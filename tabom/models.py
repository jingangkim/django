from django.db import models


class BaseModel(models.Model):
    update_at = models.DateTimeField(auto_now=True)  # 마지막 수정 시간
    created_at = models.DateTimeField(auto_now_add=True)  # 마지막 생성 시간

    class Meta:
        abstract = True


# Create your models here.
class User(BaseModel):
    name = models.CharField(max_length=50)  # 이름, 글자제한 50


class Article(BaseModel):
    title = models.CharField(max_length=255)  #


class Like(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["user", "article"], name="unique_user_article"),
        ]
