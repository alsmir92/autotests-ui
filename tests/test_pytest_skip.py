# Юзаем когда функциональность не контролируем, функциональность отключена, но нужно проверить
import pytest


@pytest.mark.skip(reason="Фича в разработке")
def test_feature_in_development():
    assert 1 == 2


@pytest.mark.skip(reason="Фича в разработке")
class TestSuiteSkip:
    def test_feature_in_development_1(self):
        ...

    def test_feature_in_development_2(self):
        ...
