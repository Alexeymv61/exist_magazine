import time

from base.base import Base

"""Класс где происходит переход в каталог аккумулторов и добавление найденного аккумулятора в корзину"""

class Product_page(Base):

    # locators
    xpath_popular = "//a[contains(@id,'lbSortPopularity')]"
    xpath_filter_options = "(//div[@class='h'])[10]"
    xpath_filter_cost = "//a[@id='ctl00_ctl00_b_b_lbSortPrice']"
    xpath_battery = "//p[text()='Exide EK700 ']"
    xpath_battery_cart = "//a[@id='394085BB_01001304e300cfdc02c915130100c83b_1043_1008']"
    xpath_battery_name = "//a[@id='ctl00_b_ctl00_hlMainLink']"
    xpath_go_to_cart = "//a[@class='basket added inbasket']"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    """find_battery - ищем аккумулятор, добавляем и переходим в корзину"""
    def find_battery_add_cart(self):
        self.get_current_url()
        self.wait_and_click_element(self.xpath_filter_cost)
        print('Товары отсортированы по цене')
        time.sleep(2)
        self.wait_and_click_element(self.xpath_popular)
        print('Товары отсортированы по популярности')
        time.sleep(1)
        self.wait_and_click_element(self.xpath_popular)
        print('Товары отсортированы по популярности')
        time.sleep(1)
        self.wait_and_click_element(self.xpath_battery)
        print('Переход на поп ап с аккумулятором - успешен')
        time.sleep(1)
        self.switch_to_frame("fancybox-frame")
        self.assert_words(self.get_element(self.xpath_battery_name), "Exide EK700")
        self.wait_and_click_element(self.xpath_battery_cart)
        print('Аккумулятор добавлен в корзину - успешно')
        self.wait_and_click_element(self.xpath_go_to_cart)
        print('Переход в корзину - успешен')
