from pages.forgot_pass_page import ForgotPassPage
from data import URLs
from locators import Locators
import allure


class TestForgotPass:

    @allure.title('Проверяем переход на страницу восстановления пароля по кнопке «Восстановить пароль»')
    def test_forgot_pass_button(self, driver):
        forgot_pass = ForgotPassPage(driver)

        forgot_pass.go_to_page(URLs.LOGIN)
        forgot_pass.click_visible_element(Locators.FORGOT_PASS_LINK)
        forgot_pass.wait_until_url_change(URLs.LOGIN)
        header = forgot_pass.get_element_text(Locators.H2_HEADER)

        assert header == 'Восстановление пароля'

    @allure.title('Проверяем ввод почты и клик по кнопке «Восстановить»')
    def test_enter_email_click_reset(self, driver):
        reset_pass = ForgotPassPage(driver)

        reset_pass.go_to_page(URLs.FORGOT_PASS)
        reset_pass.enter_random_email()
        reset_pass.click_visible_element(Locators.RESET_BUTTON)
        reset_pass.wait_until_url_change(URLs.FORGOT_PASS)
        placeholder = reset_pass.get_element_text(Locators.ENTER_CODE_PLACEHOLDER)

        assert placeholder == 'Введите код из письма'

    @allure.title('Проверяем клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его')
    def test_show_pass_active_input(self, driver):
        reset_pass = ForgotPassPage(driver)

        reset_pass.go_to_page(URLs.FORGOT_PASS)
        reset_pass.enter_random_email()
        reset_pass.click_visible_element(Locators.RESET_BUTTON)

        pass_input = reset_pass.find_visible_element(Locators.PASS_INPUT)
        before_click_input_class = pass_input.get_attribute('class')
        reset_pass.click_visible_element(Locators.SHOW_PASS_BUTTON)
        after_click_input_class = pass_input.get_attribute('class')

        assert 'input_status_active' not in before_click_input_class
        assert 'input_status_active' in after_click_input_class


