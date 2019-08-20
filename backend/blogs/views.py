# -*- coding: utf-8 -*-
# author: timor

from rest_framework import viewsets
from blogs.serializers import PostSerializer, TagSerializer, CommentSerializer
from blogs.models import Post, Tag, Comment


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_fields = ['name', 'create_time', 'publish_time', 'is_published', 'like_num', 'forward_num']


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    filter_fields = ['name']


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filter_fields = ['post__id']
