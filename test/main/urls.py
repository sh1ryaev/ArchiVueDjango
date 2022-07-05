"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from django.urls.conf import include, re_path
from django.conf.urls.static import static
from django.conf import settings
# DRF YASG
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from accounts import views

schema_view = get_schema_view(
    openapi.Info(
        title="Djoser API",
        default_version="v1",
        description="REST implementation of Django authentication system. djoser library provides a set of Django Rest Framework views to handle basic actions such as registration, login, logout, password reset and account activation. It works with custom user model.",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("admin/", admin.site.urls),
    re_path(
        r"^api/v1/docs/$",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("api/v1/", include("accounts.urls")),
    path("api/v1/", include("djoser.urls")),
    path("api/v1/", include("djoser.urls.jwt")),
    path('posts/', views.posts),
    path('posts/<int:pk>/', views.post_detail),
    path('count-like/<int:pk>/', views.addLikeCount),
    path('get-categories/', views.getCategories),
    path('user-photo/<int:pk>/', views.getUserPhoto),
    path('user-like/', views.likeUser),
    path('user-dellike/', views.dellikeUser),
    path('user-like/<int:pk>/', views.getUserLike),
    path('posts_photos/', views.postsPhotos),
    path('posts-photo/<int:pk>/', views.postsPhoto),
    path('post-search/',views.postsSearch),

]
if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)