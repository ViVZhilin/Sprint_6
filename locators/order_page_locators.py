from selenium.webdriver.common.by import By

class OrderPageLocators:
    first_name_field = [By.XPATH, ".//input[@placeholder = '* Имя']"]
    second_name_field = [By.XPATH, ".//input[@placeholder = '* Фамилия']"]
    address_field = [By.XPATH, ".//input[@placeholder = '* Адрес: куда привезти заказ']"]
    metro_station_field = [By.XPATH, ".//input[@placeholder = '* Станция метро']"]
    phone_number_field = [By.XPATH, ".//input[@placeholder = '* Телефон: на него позвонит курьер']"]
    next_button = [By.XPATH, ".//button[@class = 'Button_Button__ra12g Button_Middle__1CSJM']"]
    date_field = [By.XPATH, ".//input[@placeholder = '* Когда привезти самокат']"]
    datepicker = [By.XPATH, ".//input[@placeholder = '* Когда привезти самокат']"]
    datepicker_select = [By.XPATH, ".//div[@class = 'react-datepicker__day react-datepicker__day--008']"]

    rent_time = [By.XPATH, ".//div[@class = 'Dropdown-placeholder']"]
    rent_time_select = [By.XPATH, ".//div[@class = 'Dropdown-option']"]

    color_checkbox_black = [By.ID, "black"]
    color_checkbox_grey = [By.ID, "grey"]

    comments_field = [By.XPATH, ".//input[@placeholder = 'Комментарий для курьера']"]

    order_button = [By.XPATH, ".//button[@class = 'Button_Button__ra12g Button_Middle__1CSJM']"]
    back_button = [By.CLASS_NAME, "Button_Button__ra12g Button_Middle__1CSJM Button_Inverted__3IF-i"]

    order_id_text = [By.CLASS_NAME, "Order_Text__2broi"]

    check_status_button = [By.XPATH, ".//div[@class = 'Order_NextButton__1_rCA']/button[@class = 'Button_Button__ra12g Button_Middle__1CSJM']"]

    decline_confirmation_button = [By.LINK_TEXT, "Нет"]
    accept_confirmation_button = [By.XPATH, ".//div[@class = 'Order_Modal__YZ-d3']/div[@class = 'Order_Buttons__1xGrp']/button[@class = 'Button_Button__ra12g Button_Middle__1CSJM']"]

