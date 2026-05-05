import random

BASE_URL = "https://stellarburgers.education-services.ru/"

EXISTING_EMAIL = "thisischestnutt@ya.ru"
EXISTING_PASSWORD = "123321"

def generate_email():
    """Генератор уникального email для регистрации"""
    return f"nikita_kondratev_5_{random.randint(100, 999)}@yandex.ru"

def generate_password(length=6):
    """Генератор пароля из цифр"""
    return str(random.randint(10**(length-1), 10**length - 1))