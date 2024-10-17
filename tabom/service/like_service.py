from tabom.models import Like


def do_like(user_id: int, article_id: int) -> Like:
    return Like.objects.create(user_id=user_id, article_id=article_id)

#좋아요 취소 기능, 자신의 좋아요를 취소하기 or 좋아요가 없다면 불가능하게
def undo_like(user_id: int, article_id: int) -> None:
    # try:
    #     like = Like.objects.filter(user_id=user_id, article_id=article_id).get()  #우선 좋아요가 있는지를 가져오기 있다면? 삭제
    #     like.delete()
    # except Exception as e:
    #     print(e)
    #      쿼리를 두번 날렸다.
    Like.objects.filter(user_id=user_id, article_id=article_id).delete()
    #쿼리를 한 번만 날릴 수 있다.