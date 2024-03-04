from pages.base_page import BasePage
from locators import Locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import string


class ForgotPassPage(BasePage):

    @staticmethod
    def random_string():
        letters = string.ascii_lowercase
        random_str = ''.join(random.choice(letters)[:10] for i in range(10))
        return random_str

    def enter_random_email(self):
        self.find_visible_element(Locators.EMAIL_INPUT).send_keys(self.random_string())

    # def find_element_text_exclude(self, locator, text):
    #     return WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(locator, text))
