from pages.base_page import BasePage
from locators import Locators


class ForgotPassPage(BasePage):

    def enter_random_email(self):
        self.find_visible_element(Locators.EMAIL_INPUT).send_keys(self.random_string())
