from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators import Locators
from data import BASE_URL, EXISTING_EMAIL, EXISTING_PASSWORD


class TestLogout:

    def test_logout(self, driver):
       
        driver.get(BASE_URL + "login")
        driver.find_element(*Locators.LOGIN_EMAIL_INPUT).send_keys(EXISTING_EMAIL)
        driver.find_element(*Locators.LOGIN_PASSWORD_INPUT).send_keys(EXISTING_PASSWORD)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.ORDER_BUTTON))
        
        driver.find_element(*Locators.PERSONAL_ACCOUNT_LINK).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.LOGOUT_BUTTON))
        
        driver.find_element(*Locators.LOGOUT_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.url_contains("/login"))
        assert "/login" in driver.current_url