from django.contrib import admin
from django.http import JsonResponse
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from post.views import PostViewSet, LoginAPIView, LogoutAPIView, RegisterAPIView
from rest_framework import permissions
from rest_framework.authtoken.views import obtain_auth_token
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)

def test_api(request):
    return JsonResponse({
        "message": "Hello DRF"
    })

schema_view = get_schema_view(
    openapi.Info(
        title="Post API",
        default_version='v1',
        description="My DRF API",
    ),
    public=True,
    permission_classes=[
        permissions.AllowAny
    ],
)


router = DefaultRouter()
router.register('posts', PostViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/test/', test_api,name='test_api'),
    # path('api/posts/', PostListCreateAPIView.as_view()),
    # path('api/posts/<int:pk>/', PostDetailAPIView.as_view()),

    path('api/', include(router.urls)),
    path('api/register/', RegisterAPIView.as_view()),
    path('api/login/', LoginAPIView.as_view()),
    path('api/logout/', LogoutAPIView.as_view()),
    path('api/token/', obtain_auth_token),
    path(
        'token/',
        TokenObtainPairView.as_view()
    ),

    path(
        'token/refresh/',
        TokenRefreshView.as_view()
    ),
    path(
        'swagger/',
        schema_view.with_ui(
            'swagger',
            cache_timeout=0
        ),
    ),

]
