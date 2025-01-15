import pytest
from apps.users.serializers import CustomUserSerializer

@pytest.mark.django_db
class TestCustomUserSerializer:
    def test_valid_user_serializer(self):
        user_data = {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password': 'newpass123',
            'phone_number': '+8801700000000',
            'address': 'Dhaka, Bangladesh'
        }
        serializer = CustomUserSerializer(data=user_data)
        assert serializer.is_valid()

    def test_password_write_only(self):
        user_data = {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password': 'newpass123',
        }
        serializer = CustomUserSerializer(data=user_data)
        assert serializer.is_valid()
        assert 'password' not in serializer.data
