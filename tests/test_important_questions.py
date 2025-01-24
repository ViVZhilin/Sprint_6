import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators.main_page_locators import MainPageLocators


class TestQuestions:

    driver = None
    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.get('https://qa-scooter.praktikum-services.ru')
        cls.driver.find_element(*MainPageLocators.cookie_button).click()

    @allure.step('Проверяем открытие 1 вопроса')
    def test_question_1_open(self):
        ScrollScript = "arguments[0].scrollIntoView();"

        self.driver.execute_script(ScrollScript, self.driver.find_element(*MainPageLocators.question_1))
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located((By.ID, "accordion__heading-0")))
        self.driver.find_element(*MainPageLocators.question_1).click()

        answer_1 = self.driver.find_element(*MainPageLocators.answer_1)
        assert answer_1.text == 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'

    @allure.step('Проверяем открытие 2 вопроса')
    def test_question_2_open(self):
        ScrollScript = "arguments[0].scrollIntoView();"

        self.driver.execute_script(ScrollScript, self.driver.find_element(*MainPageLocators.question_2))
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located((By.ID, "accordion__heading-1")))
        self.driver.find_element(*MainPageLocators.question_2).click()

        answer_2 = self.driver.find_element(*MainPageLocators.answer_2)
        assert answer_2.text == 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'

    @allure.step('Проверяем открытие 3 вопроса')
    def test_question_3_open(self):
        ScrollScript = "arguments[0].scrollIntoView();"

        self.driver.execute_script(ScrollScript, self.driver.find_element(*MainPageLocators.question_3))
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located((By.ID, "accordion__heading-3")))
        self.driver.find_element(*MainPageLocators.question_3).click()

        answer_3 = self.driver.find_element(*MainPageLocators.answer_3)
        assert answer_3.text == 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'

    @allure.step('Проверяем открытие 4 вопроса')
    def test_question_4_open(self):
        ScrollScript = "arguments[0].scrollIntoView();"

        self.driver.execute_script(ScrollScript, self.driver.find_element(*MainPageLocators.question_4))
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located((By.ID, "accordion__heading-4")))
        self.driver.find_element(*MainPageLocators.question_4).click()

        answer_4 = self.driver.find_element(*MainPageLocators.answer_4)
        assert answer_4.text == 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'

    @allure.step('Проверяем открытие 5 вопроса')
    def test_question_5_open(self):
        ScrollScript = "arguments[0].scrollIntoView();"

        self.driver.execute_script(ScrollScript, self.driver.find_element(*MainPageLocators.question_5))
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located((By.ID, "accordion__heading-5")))
        self.driver.find_element(*MainPageLocators.question_5).click()

        answer_5 = self.driver.find_element(*MainPageLocators.answer_5)
        assert answer_5.text == 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'

    @allure.step('Проверяем открытие 6 вопроса')
    def test_question_6_open(self):
        ScrollScript = "arguments[0].scrollIntoView();"

        self.driver.execute_script(ScrollScript, self.driver.find_element(*MainPageLocators.question_6))
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located((By.ID, "accordion__heading-6")))
        self.driver.find_element(*MainPageLocators.question_6).click()

        answer_6 = self.driver.find_element(*MainPageLocators.answer_6)
        assert answer_6.text == 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'

    @allure.step('Проверяем открытие 7 вопроса')
    def test_question_7_open(self):
        ScrollScript = "arguments[0].scrollIntoView();"

        self.driver.execute_script(ScrollScript, self.driver.find_element(*MainPageLocators.question_7))
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located((By.ID, "accordion__heading-7")))
        self.driver.find_element(*MainPageLocators.question_7).click()

        answer_7 = self.driver.find_element(*MainPageLocators.answer_7)
        assert answer_7.text == 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'

    @allure.step('Проверяем открытие 8 вопроса')
    def test_question_8_open(self):
        ScrollScript = "arguments[0].scrollIntoView();"

        self.driver.execute_script(ScrollScript, self.driver.find_element(*MainPageLocators.question_8))
        self.driver.find_element(*MainPageLocators.question_8).click()

        answer_8 = self.driver.find_element(*MainPageLocators.answer_8)
        assert answer_8.text == 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'


    @classmethod
    def teardown_class(cls):
        cls.driver.quit()