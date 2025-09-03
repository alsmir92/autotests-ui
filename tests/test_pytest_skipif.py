# Скипается если что-то не подходит, версия системы, статус системы упал...
import pytest

SYSTEM_VERSION = 'v1.2.0'


@pytest.mark.skipif(SYSTEM_VERSION == 'v1.3.0', reason="Не может быть "
                                                       "запущен на версии "
                                                       "системы v1.3.0")
def test_system_version_valid():
    ...


@pytest.mark.skipif(SYSTEM_VERSION == 'v1.2.0', reason="Не может быть "
                                                       "запущен на версии "
                                                       "системы v1.2.0")
def test_system_version_invalid():
    ...
