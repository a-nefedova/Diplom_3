from pages.account_page import AccountPage
from data import URLs
from locators.account_page_locators import LocatorsAccount
import allure


class TestAccount:

    @allure.title('Проверяем переход по клику на «Личный кабинет»')
    def test_account_button(self, driver, registered_user):
        account = AccountPage(driver)

        account.log_in(registered_user['creds'])
        account.click_visible_element(LocatorsAccount.ACCOUNT_LINK)
        email = account.get_email()

        assert email == registered_user['creds']['email']

    @allure.title('Проверяем переход в раздел «История заказов»')
    def test_order_history(self, driver, auth_user_order):
        creds = auth_user_order['creds']
        api_order_number = auth_user_order['number']
        history = AccountPage(driver)

        history.log_in(creds)
        history.click_order_history_button()
        web_order_number = history.get_order_number(LocatorsAccount.ORDER_NUMBER_HISTORY)

        assert web_order_number == api_order_number

    @allure.title('Проверяем выход из аккаунта')
    def test_logout(self, driver, authorized_user):

        authorized_user.click_logout_button()

        assert driver.current_url == URLs.LOGIN
