from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=50)  # 이름, 글자제한 50
    update_at = models.DateTimeField(auto_now=True)  # 마지막 수정 시간
    created_at = models.DateTimeField(auto_now_add=True)  # 마지막 생성 시간


class Article(models.Model):
    title = models.CharField(max_length=255)  # 타이틀, 글자제한 50
    update_at = models.DateTimeField(auto_now=True)  # 마지막 수정 시간
    created_at = models.DateTimeField(auto_now_add=True)  # 마지막 생성 시간


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    update_at = models.DateTimeField(auto_now=True)  # 마지막 수정 시간
    created_at = models.DateTimeField(auto_now_add=True)  # 마지막 생성 시간
