from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
import allure

class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Нажимаем на кнопку заказа в хедере')
    def click_header_order_button(self):
        self.click_element(MainPageLocators.header_order_button)

    @allure.step('Нажимаем на кнопку заказа в футере')
    def click_footer_order_button(self):
        self.scroll_to_element(self.driver.find_element(*MainPageLocators.footer_order_button))
        self.click_element(MainPageLocators.footer_order_button)

    @allure.step('Нажимаем на вопрос')
    def click_question(self, question_locator):
        self.scroll_to_element(self.driver.find_element(*question_locator))
        self.click_element(question_locator)

    @allure.step('Получаем текст ответа')
    def get_answer_text(self, answer_locator):
        return self.get_element_text(answer_locator)

    @allure.step('Нажимаем на лого')
    def click_on_logo(self):
        self.click_element(MainPageLocators.main_logo)