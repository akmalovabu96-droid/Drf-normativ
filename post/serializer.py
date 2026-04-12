from rest_framework import serializers
from post.models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'title',
            'description'
        ]

    def validate_title(self, value):
        if not value.strip():
            raise serializers.ValidationError("Sarlavha bo'sh bo'lishi mumkin emas!")
        return value

    def validate(self, data):
        description = data.get("description", "")

        if len(description) < 8:
            raise serializers.ValidationError(
                "Kontent kamida 8 belgidan iborat bo'lishi shart."
            )

        return data

