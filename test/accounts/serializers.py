from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model
from rest_framework import routers,serializers,viewsets
from .models import Post, PostPhotos, UserLike, Category, CustomUserPhoto

User = get_user_model()


class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ("id", "email", "username", "first_name", "last_name", "password")



class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'id_user', 'title', 'description', 'created_at', 'like_count', 'category_id']


class PostPhotosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PostPhotos
        fields = ['id', 'id_post', 'cover']


class UserLikeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserLike
        fields = ['id_user', 'id_post']


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class UserPhotoUserNameSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    username = serializers.CharField(max_length=255)
    photo = serializers.ImageField()


class CustomUserPhotoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CustomUserPhoto
        fields = ['id','id_user','cover']