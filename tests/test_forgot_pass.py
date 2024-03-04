from pages.login_page import LoginPage
from pages.forgot_pass_page import ForgotPassPage
from data import URLs
from locators import Locators


class TestForgotPass:

    def test_forgot_pass_button(self, driver):
        forgot_pass = LoginPage(driver)

        forgot_pass.go_to_page(URLs.LOGIN)
        forgot_pass.click_visible_element(Locators.FORGOT_PASS_LINK)
        forgot_pass.wait_until_url_change(URLs.LOGIN)
        header = forgot_pass.get_element_text(Locators.H2_HEADER)

        assert header == 'Восстановление пароля'

    def test_enter_email_click_reset(self, driver):
        reset_pass = ForgotPassPage(driver)

        reset_pass.go_to_page(URLs.FORGOT_PASS)
        reset_pass.enter_random_email()
        reset_pass.click_visible_element(Locators.RESET_BUTTON)
        reset_pass.wait_until_url_change(URLs.FORGOT_PASS)
        placeholder = reset_pass.get_element_text(Locators.NOT_PASS_PLACEHOLDER)

        assert placeholder == 'Введите код из письма'

    def test_show_pass_active_input(self, driver):
        reset_pass = ForgotPassPage(driver)

        reset_pass.go_to_page(URLs.FORGOT_PASS)
        reset_pass.enter_random_email()
        reset_pass.click_visible_element(Locators.RESET_BUTTON)

        pass_input = reset_pass.find_visible_element(Locators.PASS_INPUT)
        pass_placeholder = reset_pass.find_visible_element(Locators.PASS_PLACEHOLDER)

        before_click_input_class = pass_input.get_attribute('class')
        before_click_placeholder_class = pass_placeholder.get_attribute('class')

        reset_pass.click_visible_element(Locators.SHOW_PASS_BUTTON)

        after_click_input_class = pass_input.get_attribute('class')
        after_click_placeholder_class = pass_placeholder.get_attribute('class')

        assert (('input_status_active' not in before_click_input_class)
                and ('input_status_active' in after_click_input_class))

        assert (('input__placeholder-focused' not in before_click_placeholder_class)
                and ('input__placeholder-focused' in after_click_placeholder_class))

