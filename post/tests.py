from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from rest_framework import status
from post.serializer import PostSerializer
from .models import Post
# Create your tests here.

class PostAPITest(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='akbar',
            password='12345'
        )

        self.token = Token.objects.create(user=self.user)

    def test_create_post_success(self):
        self.client.credentials(
            HTTP_AUTHORIZATION=f'Token {self.token.key}'
        )

        data = {
            "title": "Test Post",
            "description": "This is test description"
        }

        response = self.client.post(
            '/api/posts/',
            data
        )

        self.assertEqual(
            response.status_code,
            201
        )

        self.assertEqual(
            response.data['title'],
            'Test Post'
        )


    def test_serializer_validation(self):
        data = {
            "title": "",
            "description": "short"
        }

        serializer = PostSerializer(data=data)

        self.assertFalse(serializer.is_valid())

        self.assertIn('title', serializer.errors)
        self.assertIn('description', serializer.errors)


# anonymous userga yo'q
    def test_permission_denied_for_anonymous_user(self):
        data = {
            "title": "Test",
            "description": "This is description"
        }

        response = self.client.post('/api/posts/', data)
        print(response.data)

        self.assertEqual(response.status_code, 403)


    def test_get_posts(self):
        Post.objects.create(
            title='Post 1',
            description='Description 1',
            user=self.user
        )

        response = self.client.get('/api/posts/')

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            len(response.data['results']),
            1
        )


class PostIntegrationTest(APITestCase):

    def test_full_api_flow(self):

        # 1. REGISTER
        register_data = {
            "username": "akbar",
            "password": "12345",
            "confirm_password": "12345"
        }

        register_response = self.client.post(
            '/api/register/',
            register_data
        )

        self.assertEqual(
            register_response.status_code,
            status.HTTP_201_CREATED
        )

        # 2. TOKEN OLISH
        token_response = self.client.post(
            '/api/token/',
            {
                "username": "akbar",
                "password": "12345"
            }
        )

        self.assertEqual(
            token_response.status_code,
            status.HTTP_200_OK
        )

        token = token_response.data['token']

        # 3. Tokenni Headerga qo‘shish
        self.client.credentials(
            HTTP_AUTHORIZATION=f'Token {token}'
        )

        # 4. Post yaratish
        create_response = self.client.post(
            '/api/posts/',
            {
                "title": "Integration test",
                "description": "This is integration testing"
            }
        )

        self.assertEqual(
            create_response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(
            create_response.data['title'],
            'Integration test'
        )

        post_id = create_response.data['id']

        # 5. Post olish (GET)
        get_response = self.client.get(
            '/api/posts/'
        )

        self.assertEqual(
            get_response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            len(get_response.data['results']),
            1
        )

        # 6. Post UPDATE
        update_response = self.client.put(
            f'/api/posts/{post_id}/',
            {
                "title": "Updated title",
                "description": "Updated description test"
            }
        )

        self.assertEqual(
            update_response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            update_response.data['title'],
            'Updated title'
        )