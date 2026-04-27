from django.contrib import admin
from django.http import JsonResponse
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from post.views import PostListCreateAPIView, PostDetailAPIView, PostViewSet, LoginAPIView, LogoutAPIView, RegisterAPIView


def test_api(request):
    return JsonResponse({
        "message": "Hello DRF"
    })

router = DefaultRouter()
router.register('posts', PostViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/test/', test_api,name='test_api'),
    path('api/posts/', PostListCreateAPIView.as_view()),
    path('api/posts/<int:pk>/', PostDetailAPIView.as_view()),

    path('api/', include(router.urls)),
    path('api/register/', RegisterAPIView.as_view()),
    path('api/login/', LoginAPIView.as_view()),
    path('api/logout/', LogoutAPIView.as_view()),

]
