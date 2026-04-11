from django.contrib import admin
from django.http import JsonResponse
from django.urls import path

def test_api(request):
    return JsonResponse({
        "message": "Hello DRF"
    })

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/test/', test_api,name='test_api'),
]
