# -*- coding: utf-8 -*-
# author: timor

from users.models import User
from blogs.models import Post, Tag, Comment
from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):
    tags = serializers.SlugRelatedField(many=True, queryset=Tag.objects.all(), slug_field='name', allow_null=True)
    author = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='username')

    class Meta:
        model = Post
        fields = (
            'url', 'id', 'name', 'author', 'slug', 'type', 'content', 'tags', 'create_time', 'publish_time',
            'is_published', 'is_top', 'like_num', 'forward_num', 'allow_comment')


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('url', 'id', 'name')


class CommentSerializer(serializers.ModelSerializer):
    post = serializers.SlugRelatedField(queryset=Post.objects.all(), slug_field='id')
    author = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='username')

    class Meta:
        model = Comment
        fields = ('url', 'id', 'post', 'author', 'content', 'create_time')
