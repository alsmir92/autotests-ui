# Юзаем если знаем о баге и не хотим прогонять тест по этой части кода
import pytest


@pytest.mark.xfail (reason="Найден баг в приложении, из-за которого тест "
                           "падает в ошибку")
def test_with_bug():
    assert 1 == 2


@pytest.mark.xfail (reason="Баг уже исправлен, но маркировка ещё висит")
def test_without_bug():
    ...
