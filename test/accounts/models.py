from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)


class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, password=None, **extra_fields):
        if not email:
            raise ValueError("User must have an email")
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        user = self.create_user(username, email, password=password, **extra_fields)
        user.is_active = True
        user.is_staff = True
        user.is_admin = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "first_name", "last_name"]

    def get_full_name(self):
        return f"{self.first_name} - {self.last_name}"

    def get_short_name(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def __str__(self):
        return self.email


class CustomUserPhoto(models.Model):
    id_user = models.BigIntegerField()
    cover = models.ImageField(upload_to='profile_photo/%Y-%m-%d/', default='default.png')


class Post(models.Model):
    id_user = models.BigIntegerField()
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    like_count = models.IntegerField(default=0)
    category_id = models.BigIntegerField(default=1)
    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=100)

class PostPhotos(models.Model):
    id_post = models.BigIntegerField('Номер поста')
    cover = models.ImageField(upload_to='images/%Y-%m-%d/', default='default.png')


class UserLike(models.Model):
    id_user = models.BigIntegerField('Номер пользователя')
    id_post = models.BigIntegerField('Номер поста')