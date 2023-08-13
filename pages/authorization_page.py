from base.base import Base

class Authorization_page(Base):
    """Класс авторизации покупателя"""
    url = 'https://exist.ru/'

    # локаторы
    xpath_button_login = "//div[@class='h']"
    xpath_input_login = "//input[@id='login']"
    xpath_input_password = "//input[@id='pass']"
    xpath_checkbox_save_data = "//label[@for='tbSave']"
    xpath_button_user_enter = "//input[@id='btnLogin']"
    xpath_world_user_login = "//span[text()='9102736884']"
    xpath_battery_selection = "//a[@id='accumulatory']"

    def fill_login(self, element, login):
        self.get_element(element).send_keys(login)

    def fill_password(self, element, password):
        self.get_element(element).send_keys(password)

    def authorization_steps(self, login, password):
        self.driver.get(self.url)
        self.max_resolution()
        self.wait_and_click_element(self.xpath_button_login)
        print('Открытие модального окна - успешно')
        self.fill_login(self.xpath_input_login, login)
        print("Заполнение поля login - успешно")
        self.fill_password(self.xpath_input_password, password)
        print("Заполнение поля password - успешно")
        self.wait_and_click_element(self.xpath_checkbox_save_data)
        print("Клик на флаг - успешен")
        self.wait_and_click_element(self.xpath_button_user_enter)
        print("Вход - успешен")
        self.assert_words(self.get_element(self.xpath_world_user_login), "9102736884")
        self.wait_and_click_element(self.xpath_battery_selection)
