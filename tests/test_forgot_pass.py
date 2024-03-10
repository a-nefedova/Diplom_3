from pages.forgot_pass_page import ForgotPassPage
from data import URLs
from locators.forgot_pass_page_locators import LocatorsForgotPass
import allure


class TestForgotPass:

    @allure.title('Проверяем переход на страницу восстановления пароля по кнопке «Восстановить пароль»')
    def test_forgot_pass_button(self, driver):
        forgot_pass = ForgotPassPage(driver)

        forgot_pass.go_to_page(URLs.LOGIN)
        forgot_pass.click_forgot_pass()
        text_presence = bool(forgot_pass.find_element_with_text('Восстановление пароля'))

        assert text_presence

    @allure.title('Проверяем ввод почты и клик по кнопке «Восстановить»')
    def test_enter_email_click_reset(self, driver):
        reset_pass = ForgotPassPage(driver)

        reset_pass.go_to_page(URLs.FORGOT_PASS)
        reset_pass.enter_random_email()
        reset_pass.click_reset_password_button()
        text_presence = bool(reset_pass.find_element_with_text('Введите код из письма', tag='label'))

        assert text_presence

    @allure.title('Проверяем клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его')
    def test_show_pass_active_input(self, driver):
        reset_pass = ForgotPassPage(driver)

        reset_pass.go_to_reset_pass_page()
        pass_input = reset_pass.find_visible_element(LocatorsForgotPass.PASS_INPUT)
        before_click_input_class = pass_input.get_attribute('class')
        reset_pass.click_visible_element(LocatorsForgotPass.SHOW_PASS_BUTTON)
        after_click_input_class = pass_input.get_attribute('class')

        assert 'input_status_active' not in before_click_input_class
        assert 'input_status_active' in after_click_input_class
