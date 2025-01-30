import allure
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators
from selenium.webdriver.common.by import By

class OrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Заполняем поле имени')
    def enter_first_name(self, first_name):
        self.driver.find_element(*OrderPageLocators.first_name_field).send_keys(first_name)

    @allure.step('Заполняем поле фамилии')
    def enter_second_name(self, second_name):
        self.driver.find_element(*OrderPageLocators.second_name_field).send_keys(second_name)

    @allure.step('Заполняем адрес')
    def enter_address(self, address):
        self.driver.find_element(*OrderPageLocators.address_field).send_keys(address)

    @allure.step('Выбираем станцию метро')
    def select_metro_station(self):
        self.click_element(OrderPageLocators.metro_station_field)
        self.driver.find_element(By.XPATH, ".//li[@data-index='1']").click()

    @allure.step('Заполняем телефон')
    def enter_phone_number(self, phone_number):
        self.driver.find_element(*OrderPageLocators.phone_number_field).send_keys(phone_number)

    @allure.step('Нажимаем кнопку Далее')
    def click_next_button(self):
        self.click_element(OrderPageLocators.next_button)

    @allure.step('Выбираем дату аренды')
    def select_rent_date(self):
        self.click_element(OrderPageLocators.datepicker)
        self.click_element(OrderPageLocators.datepicker_select)

    @allure.step('Выбираем продолжительность аренды')
    def select_rent_duration(self):
        self.click_element(OrderPageLocators.rent_time)
        self.driver.find_element(By.XPATH, ".//div[@class='Dropdown-option']").click()

    @allure.step('Выбираем цвет самоката')
    def select_scooter_color(self):
        self.click_element(OrderPageLocators.color_checkbox_grey)

    @allure.step('Заполняем комментарий')
    def enter_comment(self, comment):
        self.driver.find_element(*OrderPageLocators.comments_field).send_keys(comment)

    @allure.step('Подтверждаем заказ')
    def confirm_order(self):
        self.click_element(OrderPageLocators.order_button)
        self.click_element(OrderPageLocators.accept_confirmation_button)

    @allure.step('Проверяем статус заказа')
    def check_order_status(self):
        self.click_element(OrderPageLocators.check_status_button)