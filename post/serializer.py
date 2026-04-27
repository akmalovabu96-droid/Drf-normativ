from rest_framework import serializers
from post.models import Post
from django.contrib.auth.models import User

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

class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError("Parollar mos emas!")

        if User.objects.filter(username=data['username']).exists():
            raise serializers.ValidationError("Username band!")

        return data

    def create(self, validated_data):
        user = User(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)