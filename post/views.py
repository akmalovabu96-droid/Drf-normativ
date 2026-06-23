from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from .models import Post
from .permission import IsOwnerOrReadOnly
from .serializer import PostSerializer, LoginSerializer, RegisterSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly
from django.contrib.auth import authenticate, login, logout
from .throttles import PostCreateThrottle
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.core.cache import cache


class PostListCreateAPIView(APIView):

    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PostSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostDetailAPIView(APIView):

    def get_object(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            return None

    def get(self, request, pk):
        post = self.get_object(pk)

        if not post:
            return Response({"error": "Post topilmadi"}, status=404)

        serializer = PostSerializer(post)
        return Response(serializer.data)

    def put(self, request, pk):
        post = self.get_object(pk)

        if not post:
            return Response({"error": "Post topilmadi"}, status=404)

        serializer = PostSerializer(post, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        post = self.get_object(pk)

        if not post:
            return Response({"error": "Post topilmadi"}, status=404)

        post.delete()
        return Response({"message": "Post o‘chirildi"}, status=204)


# class CsrfExemptSessionAuthentication(SessionAuthentication):
#     def enforce_csrf(self, request):
#         return  # CSRF tekshiruvini o'tkazib yuboradi


class PostViewSet(ModelViewSet):
    queryset = (
        Post.objects
        .select_related('user')
        .order_by('-created_at')
    )
    serializer_class = PostSerializer

    permission_classes = [
        IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
    ]

    # FILTER
    filterset_fields = [
        'title',
        'created_at'
    ]

    # SEARCH
    search_fields = [
        'title',
        'description'
    ]

    # ORDERING
    ordering_fields = [
        'created_at',
        'title'
    ]

    def get_throttles(self):
        if self.action == 'create':
            return [PostCreateThrottle()]

        return super().get_throttles()

    def perform_create(self, serializer):
        serializer.save(
            user=self.request.user
        )

        cache.clear()

    def perform_update(self, serializer):
        serializer.save()

        cache.clear()

    # Caching
    @method_decorator(cache_page(60))
    def list(self, request, *args, **kwargs):
        print("DATABASE HIT")
        return super().list(
            request,
            *args,
            **kwargs
        )

    def perform_destroy(self, instance):
        instance.delete()

        cache.clear()

class RegisterAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "User yaratildi"},
                status=status.HTTP_201_CREATED
            )

        return Response(serializer.errors, status=400)


class LoginAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)

        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']

            user = authenticate(
                request,
                username=username,
                password=password
            )

            if user:
                login(request, user)
                return Response({"message": "Tizimga kirdingiz!"})

            return Response(
                {"error": "Login yoki parol noto‘g‘ri"},
                status=401
            )

        return Response(serializer.errors, status=400)


class LogoutAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        logout(request)
        return Response({"message": "Logout qildingiz"})