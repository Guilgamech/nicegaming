from django.http import HttpResponse, response
from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response

# Create your views here.
from ..publicaciones.models import Post
from apps.api.serializers import *


class Inicio(generics.GenericAPIView):
    def get(self, request):
        url_list = {
            'list': 'list/',
            'create': 'createpost/',
            'postdetails': 'detailpost/<int:id_post>/',
        }
        return Response(url_list)


class listPost(generics.GenericAPIView):
    queryset = Post.objects.all()

    def get(self, request):
        post = Post.objects.all()
        serializer = PostSerializer(post, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class createPost(generics.GenericAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def get(self, request):
        post = Post.objects.all()
        serializer = self.serializer_class(instance=post, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data

        serializer = self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save()

            return Response(data=serializer.data, status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class detailPost(generics.GenericAPIView):
    serializer_class = PostDetailSerializer

    def get(self, request, id_post):
        post = get_object_or_404(Post, pk=id_post)
        serializer = self.serializer_class(instance=post)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id_post):
        data = request.data

        post = get_object_or_404(Post, pk=id_post)

        serializer = self.serializer_class(data=data, instance=post)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id_post):
        post = get_object_or_404(Post, pk=id_post)

        post.delete()

        return Response (status=status.HTTP_204_NO_CONTENT)
