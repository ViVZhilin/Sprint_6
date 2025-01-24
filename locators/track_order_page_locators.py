from selenium.webdriver.common.by import By

class Locators:
    decline_order_button = [By.LINK_TEXT, "Отменить заказ"]
    search_order_field = [By.XPATH, ".//input[@class = 'Input_Input__1iN_Z Track_Input__1g7lq Input_Filled__1rDxs Input_Responsible__1jDKN']"]
    view_status_button = [By.LINK_TEXT, "Посмотреть"]