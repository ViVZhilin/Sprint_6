from locators.main_page_locators import MainPageLocators


class MainPage:
    status_order_button = [*MainPageLocators.order_status_button]
    header_order_button = [*MainPageLocators.header_order_button]
    footer_order_button = [*MainPageLocators.footer_order_button]
    question_1_text = [*MainPageLocators.question_1]
    question_2_text = [*MainPageLocators.question_2]
    question_3_text = [*MainPageLocators.question_3]
    question_4_text = [*MainPageLocators.question_4]
    question_5_text = [*MainPageLocators.question_5]
    question_6_text = [*MainPageLocators.question_6]
    question_7_text = [*MainPageLocators.question_7]
    question_8_text = [*MainPageLocators.question_8]

    def __init__(self, driver):
        self.driver = driver

    def click_header_order_button(self):
        self.driver.find_element(*self.header_order_button).click()

    def click_footer_order_button(self):
        self.driver.find_element(*self.footer_order_button).click()

    def click_on_first_question_button(self):
        self.driver.find_element(*self.question_1_text).click()

    def click_on_second_question_button(self):
        self.driver.find_element(*self.question_2_text).click()

    def click_on_third_question_button(self):
        self.driver.find_element(*self.question_3_text).click()

    def click_on_fourth_question_button(self):
        self.driver.find_element(*self.question_4_text).click()

    def click_on_fifth_question_button(self):
        self.driver.find_element(*self.question_5_text).click()

    def click_on_sixth_question_button(self):
        self.driver.find_element(*self.question_6_text).click()

    def click_on_seventh_question_button(self):
        self.driver.find_element(*self.question_7_text).click()

    def click_on_eighth_question_button(self):
        self.driver.find_element(*self.question_8_text).click()


