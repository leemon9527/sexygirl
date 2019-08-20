# -*- coding: utf-8 -*-
# author: timor

from django.db import models
import datetime
import re
from uuslug import slugify
from users.models import User

BlogTypes = (
    ('text', '文字'),
    ('pic', '图片'),
    ('video', '视频'),
    ('audio', '音频'),
    ('gif', '动图'),
    ('link', '链接'),
)


class Post(models.Model):
    name = models.CharField(u'标题', max_length=150, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_author')
    slug = models.SlugField(u'链接', default='#', null=True, blank=True)
    type = models.CharField(u'类型', max_length=1, choices=BlogTypes, default='text')
    content = models.TextField(u'内容', )
    tags = models.ManyToManyField('Tag', u'标签', blank=True)

    # time
    create_time = models.DateTimeField(u'创建时间', auto_now_add=True)
    publish_time = models.DateTimeField(u'发布时间', null=True)

    # status
    is_published = models.BooleanField(u'发布', default=True)
    is_top = models.BooleanField(u'置顶', default=False)
    like_num = models.IntegerField(u'喜欢数', default=0)
    forward_num = models.IntegerField(u'转发数', default=0)
    allow_comment = models.BooleanField('开启评论', default=True)

    class Meta:
        ordering = ['-is_top', '-publish_time']
        verbose_name = u'文章'
        verbose_name_plural = u'文章'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)

        if self.is_published and not self.publish_time:
            self.publish_time = datetime.datetime.utcnow()

        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(u'标签名', max_length=50, unique=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.name = re.sub("\s", "", self.name)
        super(Tag, self).save(*args, **kwargs)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment_author')
    content = models.TextField(u'内容', )
    create_time = models.DateTimeField(u'创建时间', auto_now_add=True)

    def __str__(self):
        return self.content
