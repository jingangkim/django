from tabom.models import Like


def do_like(user_id: int, article_id: int) -> Like:
    return Like.objects.create(user_id=user_id, article_id=article_id)


# 우선 like가 있는지를 확인한다? if
