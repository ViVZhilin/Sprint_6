import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators
from locators.track_order_page_locators import Locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestOrder:

    driver = None
    first_name = "Василий"
    second_name = "Петров"
    address = "Москва"
    phone_number = "99999999999"

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.get('https://qa-scooter.praktikum-services.ru')
        cls.driver.find_element(*MainPageLocators.cookie_button).click()

    @allure.step('Оформление заказа через кнопку в хедере')
    def test_create_order_from_header(self):

        self.driver.find_element(*MainPageLocators.header_order_button).click()

        self.driver.find_element(*OrderPageLocators.first_name_field).send_keys(self.first_name)
        self.driver.find_element(*OrderPageLocators.second_name_field).send_keys(self.second_name)
        self.driver.find_element(*OrderPageLocators.address_field).send_keys(self.address)
        self.driver.find_element(*OrderPageLocators.metro_station_field).click()
        self.driver.find_element(By.XPATH, ".//li[@data-index = '1']").click()
        self.driver.find_element(*OrderPageLocators.phone_number_field).send_keys(self.phone_number)
        self.driver.find_element(*OrderPageLocators.metro_station_field).get_attribute("value")
        self.driver.find_element(*OrderPageLocators.next_button).click()



        self.driver.find_element(*OrderPageLocators.datepicker).click()
        self.driver.find_element(*OrderPageLocators.datepicker_select).click()
        self.driver.find_element(*OrderPageLocators.rent_time).click()
        self.driver.find_element(By.XPATH, ".//div[@class = 'Dropdown-option']").click()


        self.driver.find_element(*OrderPageLocators.color_checkbox_grey).click()

        self.driver.find_element(*OrderPageLocators.comments_field).send_keys("Тестовый комментарий")

        self.driver.find_element(*OrderPageLocators.order_button).click()
        self.driver.find_element(*OrderPageLocators.accept_confirmation_button).click()

        self.driver.find_element(*OrderPageLocators.check_status_button).click()

        assert self.driver.find_element(*Locators.search_order_field).get_attribute("value") != ''
        self.driver.find_element(By.CLASS_NAME, "Header_Logo__23yGT").click()
        assert self.driver.current_url == 'https://qa-scooter.praktikum-services.ru/'
        assert self.driver.find_element(By.CLASS_NAME, "Header_LogoYandex__3TSOI").get_attribute("href") == 'https://yandex.ru/'


    @allure.step('Оформление заказа через кнопку в футере')
    def test_order_from_body(self):
        ScrollScript = "arguments[0].scrollIntoView();"

        order_button_in_footer = self.driver.find_element(*MainPageLocators.footer_order_button)
        self.driver.execute_script(ScrollScript, order_button_in_footer)

        WebDriverWait(self.driver, 1).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//button[@class = 'Button_Button__ra12g Button_Middle__1CSJM']")))
        order_button_in_footer.click()

        self.driver.find_element(*OrderPageLocators.first_name_field).send_keys(self.first_name)
        self.driver.find_element(*OrderPageLocators.second_name_field).send_keys(self.second_name)
        self.driver.find_element(*OrderPageLocators.address_field).send_keys(self.address)
        self.driver.find_element(*OrderPageLocators.metro_station_field).click()
        self.driver.find_element(By.XPATH, ".//li[@data-index = '1']").click()
        self.driver.find_element(*OrderPageLocators.phone_number_field).send_keys(self.phone_number)
        self.driver.find_element(*OrderPageLocators.metro_station_field).get_attribute("value")
        self.driver.find_element(*OrderPageLocators.next_button).click()

        self.driver.find_element(*OrderPageLocators.datepicker).click()
        self.driver.find_element(*OrderPageLocators.datepicker_select).click()
        self.driver.find_element(*OrderPageLocators.rent_time).click()
        self.driver.find_element(By.XPATH, ".//div[@class = 'Dropdown-option']").click()

        self.driver.find_element(*OrderPageLocators.color_checkbox_grey).click()

        self.driver.find_element(*OrderPageLocators.comments_field).send_keys("Тестовый комментарий")

        self.driver.find_element(*OrderPageLocators.order_button).click()
        self.driver.find_element(*OrderPageLocators.accept_confirmation_button).click()

        self.driver.find_element(*OrderPageLocators.check_status_button).click()

        assert self.driver.find_element(*Locators.search_order_field).get_attribute("value") != ''

        self.driver.find_element(*MainPageLocators.main_logo).click()
        assert self.driver.current_url == 'https://qa-scooter.praktikum-services.ru/'
        assert self.driver.find_element(*MainPageLocators.main_logo_skitter).get_attribute("href") == 'https://yandex.ru/'



    @classmethod
    def teardown_class(cls):
        cls.driver.quit()