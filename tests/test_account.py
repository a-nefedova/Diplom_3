from pages.login_page import LoginPage
from data import URLs
from locators import Locators
import allure


class TestAccount:

    @allure.title('Проверяем переход по клику на «Личный кабинет»')
    def test_account_button(self, driver, registered_user):
        account = LoginPage(driver)

        account.log_in(registered_user['creds'])

        account.click_visible_element(Locators.ACCOUNT_LINK)

        email = account.get_attribute_value(Locators.ACCOUNT_EMAIL, 'value')

        assert email == registered_user['creds']['email']

    @allure.title('Проверяем переход в раздел «История заказов»')
    def test_order_history(self, driver, auth_user_order):
        creds = auth_user_order['creds']
        api_order_number = auth_user_order['number']
        history = LoginPage(driver)

        history.log_in(creds)
        history.go_to_page(URLs.ACCOUNT)
        history.click_visible_element(Locators.ORDER_HISTORY_BUTTON)
        web_raw_order_number = history.get_element_text(Locators.ORDER_NUMBER_HISTORY)
        web_order_number = int(web_raw_order_number[-5:])

        assert web_order_number == api_order_number

    @allure.title('Проверяем выход из аккаунта')
    def test_logout(self, authorized_user):

        authorized_user.click_visible_element(Locators.LOGOUT_BUTTON)
        authorized_user.wait_until_url_change(URLs.LOGGED_ACCOUNT)

        assert authorized_user.current_url() == URLs.LOGIN
