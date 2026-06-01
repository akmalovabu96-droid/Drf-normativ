# from django.contrib.auth.models import User
# from rest_framework.test import APITestCase
# from rest_framework import status
# from rest_framework.authtoken.models import Token
#
# from .models import Post
# from .serializer import PostSerializer
#
#
# class PostSerializerTest(APITestCase):

#     def test_serializer_validation(self):
#         data = {
#             'title': 'Hello',
#             'description': 'short'
#         }
#
#         serializer = PostSerializer(data=data)
#
#         self.assertFalse(serializer.is_valid())
#
#
# class PostCreateTest(APITestCase):
#
#     def setUp(self):
#         self.user = User.objects.create_user(
#             username='akbar',
#             password='12345'
#         )
#
#         self.token = Token.objects.create(user=self.user)
#
#     def test_create_post(self):
#         self.client.credentials(
#             HTTP_AUTHORIZATION='Token ' + self.token.key
#         )
#
#         data = {
#             'title': 'My test post',
#             'description': 'This is a long enough description'
#         }
#
#         response = self.client.post('/api/posts/', data)
#
#         self.assertEqual(
#             response.status_code,
#             status.HTTP_201_CREATED
#         )
#
#         self.assertEqual(
#             response.data['title'],
#             'My test post'
#         )
#
# class PermissionTest(APITestCase):
#
#     def test_unauthorized_user_cannot_create_post(self):
#
#         data = {
#             'title': 'Blocked',
#             'description': 'Unauthorized request test'
#         }
#
#         response = self.client.post('/api/posts/', data)
#
#         self.assertEqual(
#             response.status_code,
#             status.HTTP_401_UNAUTHORIZED
#         )
#
#
# class PostIntegrationTest(APITestCase):
#
#     def setUp(self):
#         self.user = User.objects.create_user(
#             username='akbar',
#             password='12345'
#         )
#
#         self.token = Token.objects.create(
#             user=self.user
#         )
#
#     def test_full_api_flow(self):
#
#         self.client.credentials(
#             HTTP_AUTHORIZATION='Token ' + self.token.key
#         )
#
#         # CREATE
#         create_response = self.client.post(
#             '/api/posts/',
#             {
#                 'title': 'Integration',
#                 'description': 'Integration testing content'
#             }
#         )
#
#         self.assertEqual(
#             create_response.status_code,
#             status.HTTP_201_CREATED
#         )
#
#         post_id = create_response.data['id']
#
#         # GET
#         get_response = self.client.get(
#             f'/api/posts/{post_id}/'
#         )
#
#         self.assertEqual(
#             get_response.status_code,
#             status.HTTP_200_OK
#         )
#
#         # UPDATE
#         update_response = self.client.put(
#             f'/api/posts/{post_id}/',
#             {
#                 'title': 'Updated title',
#                 'description': 'Updated content'
#             }
#         )
#
#         self.assertEqual(
#             update_response.status_code,
#             status.HTTP_200_OK
#         )