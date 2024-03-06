from locators import Locators
from pages.base_page import BasePage
from data import URLs
import allure


class LoginPage(BasePage):

    @allure.step('Авторизуемся в вебе')
    def log_in(self, creds):
        self.go_to_page(URLs.LOGIN)
        self.find_visible_element(Locators.EMAIL).send_keys(creds['email'])
        self.find_visible_element(Locators.PASSWORD).send_keys(creds['password'])
        self.find_visible_element(Locators.LOGIN_BUTTON).click()
        self.find_visible_element(Locators.ORDER_BUTTON)
