from django.contrib import admin
from django.http import JsonResponse
from django.urls import path
from post.views import PostListCreateAPIView, PostDetailAPIView


def test_api(request):
    return JsonResponse({
        "message": "Hello DRF"
    })

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/test/', test_api,name='test_api'),
    path('api/posts/', PostListCreateAPIView.as_view()),
    path('api/posts/<int:pk>/', PostDetailAPIView.as_view()),

]
