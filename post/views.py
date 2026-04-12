from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Post
from .serializer import PostSerializer


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