import time
from selenium import webdriver

from pages.cart_page import Cart_page
from pages.order_data_page import Order_data_page
from pages.product_page import Product_page
from pages.authorization_page import Authorization_page


def test_buy_product():
    """расписаны шаги теста в page object style"""
    driver = webdriver.Chrome(executable_path="../selenium_course/chromedriver-linux64/chromedriver")

    print("Старт")

    """создание экземпляра класса Authorization_page"""
    ap = Authorization_page(driver)
    """вызов метода authorization_steps с значениями аргументов login = '9102736884' и password = 'nKf3bsj'"""
    ap.authorization_steps('9102736884', 'nKf3bsj')

    """создание экземпляра класса Product_page"""
    pp = Product_page(driver)
    """вызываем метод find_battery_add_cart() - где ищем аккумулятор и добавляем в корзину"""
    pp.find_battery_add_cart()

    """создание экземпляра класса Cart_page"""
    cp = Cart_page(driver)
    """вызываем метод get_screenshoots_click_cart - где делаем скриншоты страницы и кликаем на кнопку прожолжить"""
    cp.get_screenshoots_click_cart()

    """создание экземпляра класса Order_data_page"""
    odp = Order_data_page(driver)
    """вызов метода complete_data_and_click_button, где выбираем способ доставки и делаем скришот страницы, кликаем на кнопку"""
    odp.complete_data_and_click_button()

    print("Финиш")
    time.sleep(5)
    driver.quit()
