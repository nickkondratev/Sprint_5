from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators import Locators
from data import generate_email, generate_password, BASE_URL


class TestRegistration:
    
    def test_successful_registration(self, driver):
        driver.get(BASE_URL + "register")
        email = generate_email()
        password = generate_password()
        
        driver.find_element(*Locators.NAME_INPUT).send_keys("Иван")
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*Locators.REGISTER_BUTTON).click()
        
        WebDriverWait(driver, 5).until(EC.url_contains("/login"))
        assert "/login" in driver.current_url

    def test_registration_invalid_password(self, driver):
        driver.get(BASE_URL + "register")
        driver.find_element(*Locators.NAME_INPUT).send_keys("Иван")
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(generate_email())
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys("12345")
        driver.find_element(*Locators.REGISTER_BUTTON).click()
        
        error = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(Locators.PASSWORD_ERROR)
        ).text
        assert "Некорректный пароль" in error