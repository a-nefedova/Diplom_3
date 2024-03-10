from pages.base_page import BasePage
from locators.forgot_pass_page_locators import LocatorsForgotPass
from data import URLs
from helper import random_string
from selenium.webdriver.common.by import By


class ForgotPassPage(BasePage):

    def enter_random_email(self):
        self.find_visible_element(LocatorsForgotPass.EMAIL_INPUT).send_keys(random_string())

    def find_element_with_text(self, text, tag='*'):
        return self.find_visible_element((By.XPATH, f'.//{tag}[text()="{text}"]'))

    def click_forgot_pass(self):
        self.click_visible_element(LocatorsForgotPass.FORGOT_PASS_LINK)
        self.wait_until_url_change(URLs.LOGIN)

    def click_reset_password_button(self):
        self.click_visible_element(LocatorsForgotPass.RESET_BUTTON)
        self.wait_until_url_change(URLs.FORGOT_PASS)

    def go_to_reset_pass_page(self):
        self.go_to_page(URLs.FORGOT_PASS)
        self.enter_random_email()
        self.click_visible_element(LocatorsForgotPass.RESET_BUTTON)
