from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.account_page_locators import LocatorsAccount
from pages.base_page import BasePage
from data import URLs
import allure


class AccountPage(BasePage):

    @allure.step('Авторизуемся в вебе')
    def log_in(self, creds):
        self.go_to_page(URLs.LOGIN)
        self.find_visible_element(LocatorsAccount.EMAIL).send_keys(creds['email'])
        self.find_visible_element(LocatorsAccount.PASSWORD).send_keys(creds['password'])
        self.find_visible_element(LocatorsAccount.LOGIN_BUTTON).click()
        self.find_visible_element(LocatorsAccount.ORDER_BUTTON)

    def click_order_button(self):
        self.click_visible_element(LocatorsAccount.ORDER_BUTTON)

    def click_order_history_button(self):
        self.go_to_page(URLs.ACCOUNT)
        self.click_visible_element(LocatorsAccount.ORDER_HISTORY_BUTTON)

    def get_order_number(self, locator):
        WebDriverWait(self.driver, 10).until_not(EC.text_to_be_present_in_element(locator, '9999'))
        web_raw_order_number = self.get_element_text(locator)
        return int(web_raw_order_number[-5:])

    def get_order_history_number(self):
        return self.get_order_number(LocatorsAccount.ORDER_NUMBER_HISTORY)

    def click_logout_button(self):
        self.click_visible_element(LocatorsAccount.LOGOUT_BUTTON)
        self.wait_until_url_change(URLs.LOGGED_ACCOUNT)

    def get_email(self):
        return self.get_attribute_value(LocatorsAccount.ACCOUNT_EMAIL, 'value')
