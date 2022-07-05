from django import forms

from accounts.models import PostPhotos, CustomUserPhoto


class PostPhotosForm(forms.ModelForm):
    class Meta:
        model = PostPhotos
        fields = ['id_post', 'cover']


class UserPhotosForm(forms.ModelForm):
    class Meta:
        model = CustomUserPhoto
        fields = ['id_user', 'cover']