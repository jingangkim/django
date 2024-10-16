from tabom.models import Like


def do_like(user_id: int, article_id: int) -> Like:
    if Like.objects.filter(user_id=user_id, article_id=article_id).exists():   #이미 있다면 exitsts하고 리턴해라, 리턴은 만들어라.
        raise Exception
    return Like.objects.create(user_id=user_id, article_id=article_id)

#우선 like가 있는지를 확인한다? if