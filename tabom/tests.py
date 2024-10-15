from django.test import TestCase


class MyTest(TestCase):

    def test(self) -> None:

        # test라는 함수는 항상 None을 리턴

        # 단일테스트 3가지 Given When Then
        # given ~를 가지고
        a = 1
        b = 3

        # When ~할 때
        result = a + b

        # # Then 결과가 ~인지?
        # try:
        self.assertEqual(result, 4)
