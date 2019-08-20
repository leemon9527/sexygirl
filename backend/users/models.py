# -*- coding: utf-8 -*-
# author: timor

from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class UserManager(BaseUserManager):
    def create_user(self, username, email=None, password=None, **extra_fields):
        """
        username 是唯一标识，没有会报错
        """

        if not username:
            raise ValueError('Users must have an username')

        if not email:
            raise ValueError('The given email must be set')

        email = UserManager.normalize_email(email)
        user = self.model(
            username=username,
            email=email,
        )
        user.set_password(password)  # 检测密码合理性
        user.save(using=self._db)  # 保存密码
        return user

    def create_superuser(self, username, email, password, **extra_fields):
        user = self.create_user(username, email, password, **extra_fields)
        user.is_admin = True  # 比创建用户多的一个字段
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    username = models.CharField(max_length=32, unique=True, db_index=True, verbose_name=u'用户名')
    email = models.EmailField(unique=True, verbose_name=u'邮箱')
    avator = models.CharField(max_length=255,
                              default='https://apic.douyucdn.cn/upload/avanew/face/201709/04/01/95a344efd1141fd073397fa78cf952ae_big.jpg')
    about = models.TextField('关于我', max_length=1000, default='', blank=True)
    roles = models.ManyToManyField('Role', blank=True, verbose_name=u'角色')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name=u'注册时间')
    create_area = models.CharField(max_length=255, verbose_name='注册地区')
    last_login_time = models.DateTimeField(auto_now_add=True, blank=True, verbose_name=u'最后登录时间')
    last_login_area = models.CharField(max_length=255, blank=True, verbose_name='最后登录地区')
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'  # 必须有一个唯一标识--USERNAME_FIELD
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username

    def get_full_name(self):
        # The user is identified by their username
        return self.username

    def get_short_name(self):
        # The user is identified by their username
        return self.username

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        return self.is_admin

    class Meta:
        verbose_name = u'用户'
        verbose_name_plural = u'用户'

    objects = UserManager()  # 创建用户


class Role(models.Model):
    name = models.CharField(max_length=64, unique=True, verbose_name=u'角色')
    desc = models.CharField(max_length=64, null=True, blank=True, verbose_name=u'描述')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u'角色'
        verbose_name_plural = u'角色'
