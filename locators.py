from selenium.webdriver.common.by import By

class Locators:
    # ===== ШАПКА (на всех страницах) =====
    
    # Ссылка «Конструктор» — ведёт на главную
    CONSTRUCTOR_LINK = (By.XPATH, "//p[contains(text(),'Конструктор')]")
    
    # Ссылка «Лента Заказов»
    ORDER_FEED_LINK = (By.XPATH, "//p[contains(text(),'Лента Заказов')]")
    
    # Логотип Stellar Burgers — кликабельный
    LOGO = (By.XPATH, "//div[contains(@class,'logo')]")
    
    # Ссылка «Личный Кабинет» — ведёт на /account
    PERSONAL_ACCOUNT_LINK = (By.XPATH, "//a[@href='/account']")


    # ===== ГЛАВНАЯ СТРАНИЦА =====
    
    # Кнопка «Войти в аккаунт» (видна, если не авторизован)
    LOGIN_TO_ACCOUNT_BUTTON = (By.XPATH, "//button[contains(text(),'Войти в аккаунт')]")
    
    # Кнопка «Оформить заказ» (видна, если авторизован)
    ORDER_BUTTON = (By.XPATH, "//button[contains(text(),'Оформить заказ')]")


    # ===== КОНСТРУКТОР (вкладки) =====
    
    # Вкладка «Булки»
    BUNS_TAB = (By.XPATH, "//span[contains(text(),'Булки')]")
    
    # Вкладка «Соусы»
    SAUCES_TAB = (By.XPATH, "//span[contains(text(),'Соусы')]")
    
    # Вкладка «Начинки»
    FILLINGS_TAB = (By.XPATH, "//span[contains(text(),'Начинки')]")
    
    # Активная (выделенная) вкладка — у неё особый класс
    ACTIVE_TAB = (By.XPATH, "//div[contains(@class,'tab_tab_type_current__')]")


    # ===== РЕГИСТРАЦИЯ (/register) =====
    
    # Поле «Имя» — первое поле ввода с name='name' на странице регистрации
    NAME_INPUT = (By.XPATH, "(//input[@name='name'])[1]")
    
    # Поле «Email» — второе поле с name='name' на странице регистрации
    EMAIL_INPUT = (By.XPATH, "(//input[@name='name'])[2]")
    
    # Поле «Пароль» — единственное поле с type='password'
    PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")
    
    # Кнопка «Зарегистрироваться»
    REGISTER_BUTTON = (By.XPATH, "//button[contains(text(),'Зарегистрироваться')]")
    
    # Ошибка под полем пароля (появляется при пароле < 6 символов)
    PASSWORD_ERROR = (By.XPATH, "//p[contains(@class,'input__error')]")


    # ===== ВХОД (/login) =====
    
    # Поле Email на странице входа (единственное поле с name="name")
    LOGIN_EMAIL_INPUT = (By.XPATH, "//input[@name='name']")
    
    # Поле Пароль на странице входа
    LOGIN_PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")
    
    # Кнопка «Войти» на странице входа
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(),'Войти')]")
    
    # Ссылка «Зарегистрироваться» на странице входа
    REGISTER_LINK = (By.XPATH, "//a[contains(text(),'Зарегистрироваться')]")
    
    # Ссылка «Войти» на странице регистрации
    LOGIN_LINK = (By.XPATH, "//a[contains(text(),'Войти')]")
    
    # Ссылка «Восстановить пароль» на странице входа
    RESTORE_PASSWORD_LINK = (By.XPATH, "//a[contains(text(),'Восстановить пароль')]")

    # ===== ВОССТАНОВЛЕНИЕ ПАРОЛЯ (/forgot-password) =====
    
    # Ссылка «Войти» на странице восстановления пароля
    RESTORE_LOGIN_LINK = (By.XPATH, "//a[contains(text(),'Войти')]")


    # ===== ЛИЧНЫЙ КАБИНЕТ (/account) =====
    
    # Кнопка «Выход»
    LOGOUT_BUTTON = (By.XPATH, "//button[contains(text(),'Выход')]")
    
    # Ссылка «Профиль» — проверка, что мы в ЛК
    PROFILE_LINK = (By.XPATH, "//a[contains(text(),'Профиль')]")