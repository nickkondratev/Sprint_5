from selenium.webdriver.common.by import By

class Locators:
    #***шапка***
    
    #конструктор
    CONSTRUCTOR_LINK = (By.XPATH, "//p[contains(text(),'Конструктор')]")
    
    #лента заказов
    ORDER_FEED_LINK = (By.XPATH, "//p[contains(text(),'Лента Заказов')]")
    
    #лого
    LOGO = (By.XPATH, "//div[contains(@class,'logo')]")
    
    #личный кабинет
    PERSONAL_ACCOUNT_LINK = (By.XPATH, "//a[@href='/account']")


    #***главная страница***
    
    #войти в аккаунт
    LOGIN_TO_ACCOUNT_BUTTON = (By.XPATH, "//button[contains(text(),'Войти в аккаунт')]")
    
    #оформить заказ
    ORDER_BUTTON = (By.XPATH, "//button[contains(text(),'Оформить заказ')]")


    #***конструктор***
    
    #булки
    BUNS_TAB = (By.XPATH, "//span[contains(text(),'Булки')]")
    
    #соусы
    SAUCES_TAB = (By.XPATH, "//span[contains(text(),'Соусы')]")
    
    #начинки
    FILLINGS_TAB = (By.XPATH, "//span[contains(text(),'Начинки')]")
    
    #актвная вкладка
    ACTIVE_TAB = (By.XPATH, "//div[contains(@class,'tab_tab_type_current__')]")


    #***регистрация***
    
    #имя
    NAME_INPUT = (By.XPATH, "(//input[@name='name'])[1]")
    
    #почта
    EMAIL_INPUT = (By.XPATH, "(//input[@name='name'])[2]")
    
    # пароль
    PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")
    
    #зарегистрироваться
    REGISTER_BUTTON = (By.XPATH, "//button[contains(text(),'Зарегистрироваться')]")
    
    #ошибка
    PASSWORD_ERROR = (By.XPATH, "//p[contains(@class,'input__error')]")


    #***вход***

    #почта
    LOGIN_EMAIL_INPUT = (By.XPATH, "//input[@name='name']")
    
    #пароль
    LOGIN_PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")
    
    #войти
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(),'Войти')]")
    
    #зарегистрироваться
    REGISTER_LINK = (By.XPATH, "//a[contains(text(),'Зарегистрироваться')]")
    
    #войти
    LOGIN_LINK = (By.XPATH, "//a[contains(text(),'Войти')]")
    
    #восстановить пароль
    RESTORE_PASSWORD_LINK = (By.XPATH, "//a[contains(text(),'Восстановить пароль')]")

    #***восстановление пароля***
    
    #войти
    RESTORE_LOGIN_LINK = (By.XPATH, "//a[contains(text(),'Войти')]")

    #***лк***
    
    #выход
    LOGOUT_BUTTON = (By.XPATH, "//button[contains(text(),'Выход')]")
    
    #профиль
    PROFILE_LINK = (By.XPATH, "//a[contains(text(),'Профиль')]")