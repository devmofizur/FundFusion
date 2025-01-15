import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from apps.users.models import CustomUser

@pytest.mark.django_db
class TestCustomUserViews:
    def setup_method(self):
        self.client = APIClient()
        self.user_data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password': 'testpass123'
        }
        self.user = CustomUser.objects.create_user(**self.user_data)
        self.admin = CustomUser.objects.create_superuser(
            username='admin',
            email='admin@example.com',
            password='adminpass123'
        )

    def test_create_user(self):
        response = self.client.post(reverse('customuser-list'), {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password': 'newpass123'
        })
        assert response.status_code == status.HTTP_201_CREATED
        assert CustomUser.objects.count() == 3  # Including the setup users

    def test_user_detail(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(reverse('customuser-detail', kwargs={'pk': self.user.id}))
        assert response.status_code == status.HTTP_200_OK
        assert response.data['username'] == self.user.username

    def test_admin_list_users(self):
        self.client.force_authenticate(user=self.admin)
        response = self.client.get(reverse('customuser-list'))
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 2  # Both setup users

    def test_non_admin_cannot_list_users(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(reverse('customuser-list'))
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_update_user(self):
        self.client.force_authenticate(user=self.user)
        update_data = {
            'email': 'updated@example.com',
            'phone_number': '+8801700000001'
        }
        response = self.client.patch(reverse('customuser-detail', kwargs={'pk': self.user.id}), update_data)
        assert response.status_code == status.HTTP_200_OK, f"Unexpected status code: {response.status_code}, data: {response.data}"

        # If PATCH doesn't work, try PUT
        if response.status_code != status.HTTP_200_OK:
            response = self.client.put(reverse('customuser-detail', kwargs={'pk': self.user.id}),
                                       {**self.user_data, **update_data})
            assert response.status_code == status.HTTP_200_OK, f"Unexpected status code: {response.status_code}, data: {response.data}"

        self.user.refresh_from_db()
        assert self.user.email == 'updated@example.com'
        assert self.user.phone_number == '+8801700000001'

