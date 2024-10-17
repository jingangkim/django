from django.db import IntegrityError
from django.test import TestCase

from tabom.models import Article, Like, User
from tabom.service.like_service import do_like, undo_like


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

    def test_like_count_should_increase(self) -> None:

        user = User.objects.create(name="test")
        article = Article.objects.create(title="test_title")

        article_count = Article.objects.count()
        #~ 할 때
        do_like(user.id, article.id)

        #~와 같은 가
        articles = Article.objects.get(id=article.id)
        self.assertEqual(1, articles.like_set.count())

    def test_a_user_can_undo_like(self) -> None:

        user = User.objects.create(name="test")
        article = Article.objects.create(title="test_title")
        like = Like.objects.create(user_id=user.id, article_id=article.id)

        undo_like(user.id, article.id)

        with self.assertRaises(Like.DoesNotExist):
            Like.objects.get(id=like.id)