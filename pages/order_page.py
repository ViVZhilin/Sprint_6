from locators.order_page_locators import OrderPageLocators

class OrderPage:
    first_name_field = [*OrderPageLocators.first_name_field]
    second_name_field = [*OrderPageLocators.second_name_field]
    address_field = [*OrderPageLocators.address_field]
    metro_station_field = [*OrderPageLocators.metro_station_field]
    phone_number_field = [*OrderPageLocators.phone_number_field]