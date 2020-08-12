from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import AlbumSerializer,CategoryModelSerializer,TaskSerializer


from .models import Album,CategoryModel,Task

#for registration 
from rest_framework import generics, permissions

# from knox.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer

# Create your views here.


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/listings/',
        'Category': '/categories/',
        'Detail View': '/task-detail/<str:pk>/',
        'Create': '/task-create/',
        'Update': '/task-update/<str:pk>/',
        'Delete': '/task-delete/<str:pk>/',
        'Createplz': '/add-plz/',
    }

    return Response(api_urls)


@api_view(['GET'])
def taskList(request):
    tasks = Album.objects.all().order_by('-id')
    serializer = AlbumSerializer(tasks, many=True)
    return Response(serializer.data)

#categories
@api_view(['GET'])
def categoryList(request):
    tasks = CategoryModel.objects.all().order_by('-id')
    serializer = CategoryModelSerializer(tasks, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def taskDetail(request, pk):
    tasks = Album.objects.get(id=pk)
    serializer = AlbumSerializer(tasks, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def taskCreate(request):
    serializer = AlbumSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def addPlz(request):
    serializer = TaskSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def taskUpdate(request, pk):
    task = Album.objects.get(id=pk)
    serializer = AlbumSerializer(instance=task, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def taskDelete(request, pk):
    task = Album.objects.get(id=pk)
    task.delete()

    return Response('Item succsesfully delete!')




# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        # "token": AuthToken.objects.create(user)[1]
        })
        
        
#https://studygyaan.com/django/django-rest-framework-tutorial-register-login-logout        