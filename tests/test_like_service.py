from django.db import IntegrityError
from django.test import TestCase

from tabom.models import Article, Like, User
from tabom.service.like_service import do_like


class TestLikeService(TestCase):

    def test_a_user_can_like_an_article(self) -> None:
        # ~를 가지고
        user = User.objects.create(name="test")
        article = Article.objects.create(title="test_title")

        # ~힐 때
        like = do_like(user.id, article.id)

        # ~과 같은가
        self.assertIsNotNone(like.id)
        self.assertEqual(user.id, like.user_id)
        self.assertEqual(article.id, like.article_id)  #

    # user는 하나의 게시글에 하나의 like만 가능하다.
    def test_a_user_can_not_like_an_article_only_once(self) -> None:
        # given
        user = User.objects.create(name="test")
        article = Article.objects.create(title="test_title")

        do_like(user.id, article.id)
        with self.assertRaises(IntegrityError):
            do_like(user.id, article.id)
