from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators import Locators
from data import BASE_URL


class TestConstructor:

    def test_sauces_tab(self, driver):
        driver.get(BASE_URL)
        driver.find_element(*Locators.SAUCES_TAB).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.ACTIVE_TAB))
        active_tab = driver.find_element(*Locators.ACTIVE_TAB).text
        assert "Соусы" in active_tab

    def test_fillings_tab(self, driver):
        driver.get(BASE_URL)
        driver.find_element(*Locators.FILLINGS_TAB).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.ACTIVE_TAB))
        active_tab = driver.find_element(*Locators.ACTIVE_TAB).text
        assert "Начинки" in active_tab

    def test_buns_tab(self, driver):
        driver.get(BASE_URL)
        driver.find_element(*Locators.SAUCES_TAB).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.ACTIVE_TAB))
        driver.find_element(*Locators.BUNS_TAB).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.ACTIVE_TAB))
        active_tab = driver.find_element(*Locators.ACTIVE_TAB).text
        assert "Булки" in active_tab