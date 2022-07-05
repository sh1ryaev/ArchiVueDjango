from django.contrib import admin

# Register your models here.
from .models import CustomUser, Post, PostPhotos, UserLike, Category, CustomUserPhoto

admin.site.register(CustomUser)
admin.site.register(Post)
admin.site.register(PostPhotos)
admin.site.register(UserLike)
admin.site.register(Category)
admin.site.register(CustomUserPhoto)





