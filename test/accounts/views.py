from django.core.paginator import Paginator
from django.template.loader import render_to_string
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from .forms import PostPhotosForm, UserPhotosForm
from .serializers import PostSerializer, PostPhotosSerializer, UserLikeSerializer, CategorySerializer, \
    UserPhotoUserNameSerializer, CustomUserPhotoSerializer
from .models import Post, PostPhotos, UserLike, Category, CustomUserPhoto, CustomUser
from django.db.models import Q

@csrf_exempt
def posts(request):
    if(request.method == 'GET'):
        # get all the tasks
        posts = Post.objects.all()
        # serialize the task data
        cat_id = request.GET.get('cat_id', None)
        cat_id = cat_id.split('%')
        searchWord = request.GET.get('search', '')
        if searchWord=='null':
            searchWord=''
        print(cat_id)
        print(searchWord)
        if len(searchWord)>0 and cat_id[0]!='':
            print(1)
            posts = Post.objects.filter(Q(title__icontains=searchWord) | Q(description__icontains=searchWord)&Q(category_id__in=cat_id))
        elif len(searchWord)>0:
            print(2)
            posts = Post.objects.filter(Q(title__icontains=searchWord)|Q(description__icontains=searchWord))
        elif cat_id[0]!='':
            print(3)
            posts = Post.objects.filter(category_id__in=cat_id)
        paginator = Paginator(posts, 10)
        page = request.GET.get('page', 1)
        print(page)
        serializer = PostSerializer(paginator.get_page(int(page)), many=True)
        # return a Json response
        return JsonResponse(serializer.data,safe=False)
    elif(request.method == 'POST'):
        # parse the incoming information
        data = JSONParser().parse(request)
        # instanciate with the serializer
        serializer = PostSerializer(data=data)
        # check if the sent information is okay
        if(serializer.is_valid()):
            # if okay, save it on the database
            serializer.save()
            # provide a Json Response with the data that was saved
            return JsonResponse(serializer.data, status=201)
            # provide a Json Response with the necessary error information
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def post_detail(request, pk):
    try:
        # obtain the task with the passed id.
        posts = Post.objects.get(pk=pk)
        print(posts)
    except:
        # respond with a 404 error message
        return HttpResponse(status=404)
    if (request.method == 'GET'):
        # get all the tasks
        posts = Post.objects.filter(pk=pk)
        # serialize the task data
        serializer = PostSerializer(posts, many=True)
        # return a Json response
        return JsonResponse(serializer.data, safe=False)
    elif(request.method == 'PUT'):
        # parse the incoming information
        data = JSONParser().parse(request)
        print(data)
        # instanciate with the serializer
        serializer = PostSerializer(posts, data=data)
        # check whether the sent information is okay
        if(serializer.is_valid()):
            # if okay, save it on the database
            serializer.save()
            # provide a JSON response with the data that was submitted
            return JsonResponse(serializer.data, status=201)
        # provide a JSON response with the necessary error information
        return JsonResponse(serializer.errors, status=400)
    elif(request.method == 'DELETE'):
        # delete the task
        posts.delete()
        # return a no content response.
        return HttpResponse(status=204)


@csrf_exempt
def postsSearch(request):
    if (request.method == 'GET'):
        searchWord = request.GET.get('searchWord', None)
        posts = Post.objects.filter(Q(title__icontains=searchWord)|Q(description__icontains=searchWord))
        # serialize the task data
        serializer = PostSerializer(posts, many=True)
        # return a Json response
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def postsPhotos(request):
    if(request.method == 'GET'):
        # get all the tasks
        photos = PostPhotos.objects.all()
        # serialize the task data
        serializer = PostPhotosSerializer(photos, many=True)
        # return a Json response
        return JsonResponse(serializer.data,safe=False)
    elif(request.method == 'POST'):
        data = {}
        form = PostPhotosForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            return JsonResponse(data)
        else:
            data['form_is_valid'] = False
            data['picture_form'] = render_to_string("picha/picture_form.html",
                                                    {'form': form}, request=request)

    data['picture_form'] = render_to_string("picha/picture_form.html",
                                            {'form': form}, request=request)
    return JsonResponse(data)


@csrf_exempt
def postsPhoto(request,pk):
    if(request.method == 'GET'):
        # get all the tasks
        photos = PostPhotos.objects.filter(id_post=pk)
        # serialize the task data
        serializer = PostPhotosSerializer(photos, many=True)
        # return a Json response
        return JsonResponse(serializer.data,safe=False)


@csrf_exempt
def addLikeCount(request, pk):
    post = Post.objects.get(pk=pk)
    post.like_count+=1
    post.save()
    serializer = PostSerializer(post)
    # return a Json response
    return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def likeUser(request):
    if (request.method == 'POST'):
        # parse the incoming information
        data = JSONParser().parse(request)
        # instanciate with the serializer
        serializer = UserLikeSerializer(data=data)
        # check if the sent information is okay
        if (serializer.is_valid()):
            # if okay, save it on the database
            serializer.save()
            post = Post.objects.get(pk=data['id_post'])
            post.like_count += 1
            post.save()
            # provide a Json Response with the data that was saved
            return JsonResponse(serializer.data, status=201)
            # provide a Json Response with the necessary error information
        return JsonResponse(serializer.errors, status=400)
    elif (request.method == 'DELETE'):
        # parse the incoming information
        data = JSONParser().parse(request)
        # instanciate with the serializer
        serializer = UserLikeSerializer(data=data)
        # check if the sent information is okay
        if (serializer.is_valid()):
            # if okay, save it on the database
            serializer.save()
            post = Post.objects.get(pk=data['id_post'])
            post.like_count -= 1
            post.save()
            userLike = UserLike.objects.filter(id_post=data['id_post'],id_user=data['id_user'])
            # delete the task
            userLike.delete()
            # provide a Json Response with the data that was saved
            return JsonResponse(serializer.data, status=201)
            # provide a Json Response with the necessary error information
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def dellikeUser(request):
    if (request.method == 'POST'):
        # parse the incoming information
        data = JSONParser().parse(request)
        # instanciate with the serializer
        serializer = UserLikeSerializer(data=data)
        # check if the sent information is okay
        if (serializer.is_valid()):
            # if okay, save it on the database
            serializer.save()
            post = Post.objects.get(pk=data['id_post'])
            post.like_count -= 1
            post.save()
            userLike = UserLike.objects.filter(id_post=data['id_post'],id_user=data['id_user'])
            # delete the task
            userLike.delete()
            # provide a Json Response with the data that was saved
            return JsonResponse(serializer.data, status=201)
            # provide a Json Response with the necessary error information
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def getUserLike(request, pk):
    if(request.method=='GET'):
        post = UserLike.objects.filter(id_user=pk)
        serializer = UserLikeSerializer(post, many=True)
        # return a Json response
        return JsonResponse(serializer.data, safe=False, status=201)
    elif(request.method=='DELETE'):
        post = UserLike.objects.filter(id_post=pk)
        # delete the task
        post.delete()
        # return a no content response.
        return HttpResponse(status=204)


@csrf_exempt
def getCategories(request):
    if(request.method=='GET'):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        # return a Json response
        return JsonResponse(serializer.data, safe=False, status=201)


@csrf_exempt
def getUserPhoto(request,pk):
    if (request.method == 'GET'):
        photo = CustomUserPhoto.objects.get(id_user=pk)
        username = CustomUser.objects.get(id=pk)
        UPUN=UserPhotoUserName(id=username.id,username=username.username,photo=photo.cover)
        serializer = UserPhotoUserNameSerializer(UPUN)
        return JsonResponse(serializer.data,safe=False, status=201)
    elif(request.method == 'POST'):
        try:
            userPhoto = CustomUserPhoto.objects.get(id_user=pk)
            userPhoto.delete()
        except: pass
        data = {}
        form = UserPhotosForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            return JsonResponse(data)
        else:
            data['form_is_valid'] = False
            data['picture_form'] = render_to_string("picha/picture_form.html",
                                                    {'form': form}, request=request)

    data['picture_form'] = render_to_string("picha/picture_form.html",
                                            {'form': form}, request=request)
    return JsonResponse(data)


class UserPhotoUserName:
    def __init__(self, id, username,photo):
            self.id=id
            self.username=username
            self.photo=photo