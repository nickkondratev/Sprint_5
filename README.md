# Sprint_5

автотесты для stellar burgers на selenium и python

tests/ - папка с тестами
- conftest.py - настройка браузера (открывает и закрывает Chrome)
- test_registration.py - регистрация
- test_login.py - вход 4 способами
- test_personal_account.py - личный кабинет
- test_logout.py - выход
- test_constructor.py - конструктор бургера

locators.py - все локаторы с комментариями

data.py - ссылка на сайт, генератор email и пароль для тестов

## запуск

py -m pip install selenium
py -m pytest -v tests/