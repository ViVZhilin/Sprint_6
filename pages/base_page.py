from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    @allure.step('Открываем сайт')
    def open_site(self, url):
        self.driver.get(url)

    @allure.step('Нажимаем кнопку куки')
    def accept_cookies(self, locator):
        self.driver.find_element(*locator).click()

    @allure.step('Скролл до элемента')
    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Клик по элементу')
    def click_element(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.click()

    @allure.step('Получение текста элемента')
    def get_element_text(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element.text

    @allure.step('Клик по логотипу')
    def click_logo(self, locator):
        self.click_element(locator)

    @allure.step('Проверка текущего URL')
    def check_current_url(self, expected_url):
        current_url = self.driver.current_url
        assert current_url == expected_url, f"Ожидаемый URL: {expected_url}, Фактический URL: {current_url}"