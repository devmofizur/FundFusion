from rest_framework import status, serializers
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.conf import settings
import random
import logging
from django.core.cache import cache

logger = logging.getLogger(__name__)
User = get_user_model()

# Custom Serializer to use 'email' for authentication
class CustomTokenObtainPairSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if not email or not password:
            raise serializers.ValidationError({'detail': 'Email and password are required'})

        try:
            # Fetch the user using email
            user = User.objects.get(email=email)

            # Verify the password
            if not user.check_password(password):
                raise serializers.ValidationError({'detail': 'Invalid email or password'})
        except User.DoesNotExist:
            raise serializers.ValidationError({'detail': 'Invalid email or password'})

        # Generate tokens for the user
        refresh = RefreshToken.for_user(user)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'user': {
                'id': user.id,
                'email': user.email,
                'username': user.username,
                'is_admin': user.is_admin,
            }
        }


# Override TokenObtainPairView to use the custom serializer
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class CustomTokenRefreshView(TokenRefreshView):
    """
    Custom view for token refresh, inherits from TokenRefreshView.
    Currently no custom behavior, but can be extended later.
    """
    pass


class LogoutView(APIView):
    def post(self, request):
        try:
            refresh_token = request.data.get('refresh_token')  # Expect refresh token in request body
            if refresh_token:
                token = RefreshToken(refresh_token)
                token.blacklist()  # Blacklist the token to log out the user
                logger.info("User logged out successfully.")
                return Response({'message': 'Successfully logged out'}, status=status.HTTP_200_OK)

            logger.warning("Refresh token not provided in logout request.")
            return Response({'error': 'Refresh token required'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.error(f"Logout error: {str(e)}")
            return Response({'error': 'Invalid token or an error occurred'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    try:
        data = request.data

        # Validate all required fields
        if not all(key in data for key in ('email', 'password', 'confirm_password')):
            return Response({'error': 'Email, password, and confirm_password are required'}, status=status.HTTP_400_BAD_REQUEST)

        # Validate email uniqueness
        if User.objects.filter(email=data['email']).exists():
            return Response({'error': 'Email already registered'}, status=status.HTTP_400_BAD_REQUEST)

        # Validate password match
        if data['password'] != data['confirm_password']:
            return Response({'error': 'Passwords do not match'}, status=status.HTTP_400_BAD_REQUEST)

        # Validate password strength
        if len(data['password']) < 8:
            return Response({'error': 'Password must be at least 8 characters long'}, status=status.HTTP_400_BAD_REQUEST)

        # Create the user
        user = User.objects.create_user(
            username=data.get('username', ''),  # Optional username
            email=data['email'],
            password=data['password']
        )

        refresh = RefreshToken.for_user(user)
        logger.info(f"New user registered: {user.email}")

        return Response({
            'access': str(refresh.access_token),
            'refresh': str(refresh),
            'user': {
                'id': user.id,
                'email': user.email,
                'username': user.username,
                'is_admin': user.is_admin
            }
        })
    except Exception as e:
        logger.error(f"Registration error: {str(e)}")
        return Response({'error': 'Registration failed'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([AllowAny])
def forgot_password(request):
    email = request.data.get('email')
    try:
        user = User.objects.get(email=email)

        # Rate limiting
        cache_key = f"password_reset_{user.id}"
        if cache.get(cache_key):
            return Response(
                {'error': 'Please wait before requesting another OTP'},
                status=status.HTTP_429_TOO_MANY_REQUESTS
            )

        # Generate OTP
        otp = ''.join([str(random.randint(0, 9)) for _ in range(6)])

        # Store OTP in cache with expiration
        otp_cache_key = f"otp_{user.id}"
        cache.set(otp_cache_key, otp, timeout=300)  # 5 minutes expiration

        # Set rate limiting
        cache.set(cache_key, True, timeout=60)  # 1 minute cooldown

        # Send email
        send_mail(
            'Password Reset OTP',
            f'''Your OTP for password reset is: {otp}
            This OTP will expire in 5 minutes.
            If you did not request this reset, please ignore this email.''',
            settings.DEFAULT_FROM_EMAIL,
            [email],
            fail_silently=False,
        )

        logger.info(f"Password reset OTP sent to: {email}")
        return Response({'message': 'OTP sent successfully'})

    except User.DoesNotExist:
        logger.warning(f"Password reset attempted for non-existent email: {email}")
        # Return success even if user doesn't exist to prevent email enumeration
        return Response({'message': 'If an account exists, an OTP has been sent'})

    except Exception as e:
        logger.error(f"Password reset error: {str(e)}")
        return Response(
            {'error': 'Failed to process request'},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


@api_view(['POST'])
@permission_classes([AllowAny])
def verify_otp(request):
    email = request.data.get('email')
    otp = request.data.get('otp')
    new_password = request.data.get('new_password')

    try:
        user = User.objects.get(email=email)
        otp_cache_key = f"otp_{user.id}"
        stored_otp = cache.get(otp_cache_key)

        if not stored_otp or stored_otp != otp:
            return Response(
                {'error': 'Invalid or expired OTP'},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Validate new password
        if len(new_password) < 8:
            return Response(
                {'error': 'Password must be at least 8 characters long'},
                status=status.HTTP_400_BAD_REQUEST
            )

        user.set_password(new_password)
        user.save()
        cache.delete(otp_cache_key)

        logger.info(f"Password reset successful for user: {email}")
        return Response({'message': 'Password reset successful'})

    except User.DoesNotExist:
        return Response(
            {'error': 'User not found'},
            status=status.HTTP_404_NOT_FOUND
        )
    except Exception as e:
        logger.error(f"OTP verification error: {str(e)}")
        return Response(
            {'error': 'Failed to process request'},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


class AdminOnlyView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        if not request.user.is_admin:
            return Response({'error': 'Admin access required'}, status=403)
        return Response({'message': 'Welcome, Admin!'})
