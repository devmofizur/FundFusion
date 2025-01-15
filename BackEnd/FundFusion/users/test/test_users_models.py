import pytest
from apps.users.models import CustomUser

@pytest.mark.django_db
class TestCustomUserModel:
    def test_create_user(self):
        user = CustomUser.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        assert user.username == 'testuser'
        assert user.email == 'test@example.com'
        assert user.is_active == True
        assert user.is_staff == False
        assert user.is_admin == False

    def test_create_superuser(self):
        admin = CustomUser.objects.create_superuser(
            username='admin',
            email='admin@example.com',
            password='adminpass123'
        )
        assert admin.username == 'admin'
        assert admin.email == 'admin@example.com'
        assert admin.is_active == True
        assert admin.is_staff == True
        assert admin.is_superuser == True
