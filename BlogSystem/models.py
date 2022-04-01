import re
import uuid

from django.core.exceptions import ValidationError
from django.db import models

# Define your validators here.


def validate_name(name):
    if re.match('^[a-zA-Z0-9]{,12}$', name):
        return name
    elif User.objects.filter(name=name).exists():
        raise ValidationError("This username is already in use.")
    else:
        raise ValidationError("Username format error")


def validate_password(password):
    if re.match("^(?=.*[0-9])(?=.*[a-zA-Z])(.{8,16})$", password):
        return password
    else:
        return ValidationError("Please enter the password in a correct format")

# Create your models here.
# 关于User类的具体校验规则定义如下
# 1.name不能和数据库内已经定义的用户名重复，字母和数字组成，长度在12位以内
# 2.


class User(models.Model):
    # 身份的唯一标识符
    id = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        primary_key=True,
        editable=False
    )
    # 用户姓名
    name = models.CharField(max_length=12, validators=[validate_name])
    password = models.CharField(max_length=20, validators=[validate_password])
    created = models.DateTimeField(auto_now_add=True)
    description = models.TextField(null=True, blank=True)
    tags = models.ManyToManyField('Tag', blank=True)
    avatar = models.ImageField(
        upload_to='users/',
        default='default.jpg',
        null=True,
        blank=True)

    def __str__(self):
        return self.name


class Article(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        primary_key=True,
        editable=False
    )
    title = models.CharField(max_length=40)
    # 副标题可以为空
    sub_title = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    tags = models.ManyToManyField('Tag', blank=True)
    content = models.TextField(null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(
        upload_to='articles/',
        default='default.jpg',
        null=True,
        blank=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return self.title


class Tag(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        primary_key=True,
        editable=False
    )
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

# 到目前为止，models.py基本已经完善了，只要后续再添加一个图像页面即可
