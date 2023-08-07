import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.cart_page import Cart_page
from pages.order_data_page import Order_data_page
from pages.product_page import Product_page
from pages.authorization_page import Authorization_page


def test_buy_product():
    """расписаны шаги теста в page object style"""
    driver = webdriver.Chrome(executable_path="/home/abalashov/selenium_course/chromedriver-linux64/chromedriver")

    print("Старт")

    """создание экземпляра класса Authorization_page"""
    ap = Authorization_page(driver)
    """вызов метода authorization_steps с значениями аргументов login = '9102736884' и password = 'nKf3bsj'"""
    ap.authorization_steps('9102736884', 'nKf3bsj')

    """создание экземпляра класса Product_page"""
    pp = Product_page(driver)
    """вызов метода find_battery_add_cart"""
    pp.find_battery_add_cart()

    """создание экземпляра класса Cart_page"""
    cp = Cart_page(driver)
    """вызов метода find_battery_add_cart"""
    cp.find_battery_add_to_cart()

    """создание экземпляра класса Order_data_page"""
    odp = Order_data_page(driver)
    """вызов метода find_battery_add_cart"""
    odp.complete_data_and_click_button()

    print("Финиш")
    time.sleep(5)
    driver.quit()
