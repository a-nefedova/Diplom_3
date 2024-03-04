from pages.base_page import BasePage
from data import URLs
from locators import Locators

from time import sleep


class TestAccount:

    def test_account_button(self, driver, registered_user):
        account = BasePage(driver)

        account.go_to_page(URLs.LOGIN)
        account.log_in(registered_user['creds'])

        account.find_visible_element(Locators.ORDER_BUTTON)

        account.click_visible_element(Locators.ACCOUNT_LINK)
        email_value = account.find_visible_element(Locators.ACCOUNT_EMAIL).get_attribute("value")

        assert email_value == registered_user['creds']['email']

    def test_order_history(self, authorized_user):

        authorized_user.click_visible_element(Locators.ORDER_HISTORY_BUTTON)

        sleep(5)

    def test_logout(self, authorized_user):

        authorized_user.click_visible_element(Locators.LOGOUT_BUTTON)
        authorized_user.wait_until_url_change(URLs.LOGGED_ACCOUNT)

        assert authorized_user.current_url() == URLs.LOGIN
