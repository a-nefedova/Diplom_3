import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import string


class BasePage:

    @allure.step('Открываем браузер')
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Переходим на страницу')
    def go_to_page(self, url):
        self.driver.get(url)

    def find_visible_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator))

    def find_visible_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.visibility_of_all_elements_located(locator))

    def click_visible_element(self, locator, time=10):
        self.find_visible_element(locator, time).click()

    def get_element_text(self, locator):
        return self.find_visible_element(locator).text

    def wait_until_url_change(self, url):
        WebDriverWait(self.driver, 5).until(EC.url_changes(url))

    def current_url(self):
        return self.driver.current_url

    @staticmethod
    def random_string():
        letters = string.ascii_lowercase
        random_str = ''.join(random.choice(letters)[:10] for i in range(10))
        return random_str

    def find_element_text_exclude(self, locator, text):
        return WebDriverWait(self.driver, 10).until_not(EC.text_to_be_present_in_element(locator, text))

    @staticmethod
    def valid_creds():
        creds = {
            'email': f'{BasePage.random_string()}@yandex.ru',
            'password': BasePage.random_string(),
            'name': BasePage.random_string()
        }
        return creds

    def order_number_list(self, locator):
        order_list = self.find_visible_elements(locator)
        order_number_list = []
        number = None
        for order in order_list:
            try:
                number = int(order.text[-5:])
            except Exception as e:
                if type(e) is ValueError:
                    return order_number_list
            order_number_list.append(number)
        return order_number_list

    def get_attribute_value(self, locator, attribute):
        return self.find_visible_element(locator).get_attribute(attribute)
