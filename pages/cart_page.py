import time
from base.base import Base


class Cart_page(Base):
    """Класс где происходит переход в каталог аккумулторов и добавление найденного аккумулятора в корзину"""
    # locators
    xpath_button_continue = "//a[contains(@id, 'slbInvokeSubmit')]"

    def get_screenshoots_click_cart(self):
        """На странице "корзина" кликаем на кнопку продолжить оформление"""
        self.get_current_url()
        time.sleep(1)
        self.make_screenshoot('cart_page_header')
        self.scroll_on_page(0, 700)
        time.sleep(1)
        self.make_screenshoot('cart_page_footer')
        self.wait_and_click_element(self.xpath_button_continue)
