from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators import Locators
from data import BASE_URL, EXISTING_EMAIL, EXISTING_PASSWORD


class TestLogin:

    def login_user(self, driver):
        driver.find_element(*Locators.LOGIN_EMAIL_INPUT).send_keys(EXISTING_EMAIL)
        driver.find_element(*Locators.LOGIN_PASSWORD_INPUT).send_keys(EXISTING_PASSWORD)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.ORDER_BUTTON))

    def test_login_from_main_page(self, driver):
        driver.get(BASE_URL)
        driver.find_element(*Locators.LOGIN_TO_ACCOUNT_BUTTON).click()
        self.login_user(driver)
        assert driver.find_element(*Locators.ORDER_BUTTON).is_displayed()

    def test_login_from_personal_account(self, driver):
        driver.get(BASE_URL)
        driver.find_element(*Locators.PERSONAL_ACCOUNT_LINK).click()
        self.login_user(driver)
        assert driver.find_element(*Locators.ORDER_BUTTON).is_displayed()

    def test_login_from_registration_form(self, driver):
        driver.get(BASE_URL + "register")
        driver.find_element(*Locators.LOGIN_LINK).click()
        self.login_user(driver)
        assert driver.find_element(*Locators.ORDER_BUTTON).is_displayed()

    def test_login_from_password_recovery(self, driver):
        driver.get(BASE_URL + "forgot-password")
        driver.find_element(*Locators.RESTORE_LOGIN_LINK).click()
        self.login_user(driver)
        assert driver.find_element(*Locators.ORDER_BUTTON).is_displayed()