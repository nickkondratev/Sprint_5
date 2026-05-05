# Sprint_5 
## описание
проект содержит автотесты для сервиса stellar burgers(https://stellarburgers.education-services.ru/) нв python и selenium

## структура
- `tests/` — тесты по функциональности
- `locators.py` — локаторы элементов 
- `data.py` — URL, генератор email/пароля, данные для входа
- `conftest.py` — фикстура driver (открывает и закрывает Chrome)
  
## установка
```bash
py -m pip install selenium
