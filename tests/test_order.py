import allure
import pytest
from data.data import Data
from locators.main_page_locators import MainPageLocators
from pages.main_page import MainPage
from pages.order_page import OrderPage
from pages.base_page import BasePage

@pytest.mark.usefixtures("driver")
class TestOrder:
    @allure.title('Оформление заказа через кнопку в хедере')
    def test_create_order_from_header(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        base_page = BasePage(driver)

        main_page.open_site(Data.url)
        base_page.accept_cookies()
        main_page.click_header_order_button()

        order_page.enter_first_name(Data.first_name)
        order_page.enter_second_name(Data.second_name)
        order_page.enter_address(Data.address)
        order_page.select_metro_station()
        order_page.enter_phone_number(Data.phone_number)
        order_page.click_next_button()

        order_page.select_rent_date()
        order_page.select_rent_duration()
        order_page.select_scooter_color()
        order_page.enter_comment("Тестовый комментарий")
        order_page.confirm_order()

        assert order_page.check_order_status() != ''
        main_page.click_on_logo()  # Используем метод страницы без передачи локатора
        base_page.check_current_url()  # Проверка URL через метод страницы



    @allure.title('Оформление заказа через кнопку в футере')
    def test_create_order_from_footer(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        base_page = BasePage(driver)

        main_page.open_site(Data.url)
        main_page.click_footer_order_button()

        order_page.enter_first_name(Data.first_name)
        order_page.enter_second_name(Data.second_name)
        order_page.enter_address(Data.address)
        order_page.select_metro_station()
        order_page.enter_phone_number(Data.phone_number)
        order_page.click_next_button()

        order_page.select_rent_date()
        order_page.select_rent_duration()
        order_page.select_scooter_color()
        order_page.enter_comment("Тестовый комментарий")
        order_page.confirm_order()

        assert order_page.check_order_status() != ''
        main_page.click_on_logo()  # Используем метод страницы без передачи локатора
        base_page.check_current_url()  # Проверка URL через метод страницы
