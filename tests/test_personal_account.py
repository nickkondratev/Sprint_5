from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators import Locators
from data import BASE_URL, EXISTING_EMAIL, EXISTING_PASSWORD


class TestPersonalAccount:

    def test_go_to_personal_account(self, driver):
        driver.get(BASE_URL + "login")
        driver.find_element(*Locators.LOGIN_EMAIL_INPUT).send_keys(EXISTING_EMAIL)
        driver.find_element(*Locators.LOGIN_PASSWORD_INPUT).send_keys(EXISTING_PASSWORD)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.ORDER_BUTTON))
        
        driver.find_element(*Locators.PERSONAL_ACCOUNT_LINK).click()
        WebDriverWait(driver, 5).until(EC.url_contains("/account"))
        assert "/account" in driver.current_url

    def test_go_to_constructor_from_account(self, driver):
        driver.get(BASE_URL + "login")
        driver.find_element(*Locators.LOGIN_EMAIL_INPUT).send_keys(EXISTING_EMAIL)
        driver.find_element(*Locators.LOGIN_PASSWORD_INPUT).send_keys(EXISTING_PASSWORD)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.ORDER_BUTTON))
        
        driver.find_element(*Locators.PERSONAL_ACCOUNT_LINK).click()
        WebDriverWait(driver, 5).until(EC.url_contains("/account"))
        
        driver.find_element(*Locators.CONSTRUCTOR_LINK).click()
        WebDriverWait(driver, 5).until(EC.url_to_be(BASE_URL))
        assert driver.current_url == BASE_URL

    def test_go_to_main_by_logo(self, driver):

        driver.get(BASE_URL + "login")
        driver.find_element(*Locators.LOGIN_EMAIL_INPUT).send_keys(EXISTING_EMAIL)
        driver.find_element(*Locators.LOGIN_PASSWORD_INPUT).send_keys(EXISTING_PASSWORD)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.ORDER_BUTTON))
        
        driver.find_element(*Locators.PERSONAL_ACCOUNT_LINK).click()
        WebDriverWait(driver, 5).until(EC.url_contains("/account"))
        
        driver.find_element(*Locators.LOGO).click()
        WebDriverWait(driver, 5).until(EC.url_contains("/"))
        
        assert "/account" not in driver.current_url