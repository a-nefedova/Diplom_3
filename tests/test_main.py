from pages.base_page import BasePage
from data import URLs
from locators import Locators
import allure
from selenium.webdriver import ActionChains
import pytest


class TestMain:

    @allure.title('Проверяем переход по клику на кнопки «Конструктор» и «Лента заказов»')
    @allure.description('Используем параметризацию для кнопок')
    @pytest.mark.parametrize('url,button,header',
                             [[URLs.ORDER_FEED, Locators.CONSTRUCTOR_BUTTON, "Соберите бургер"],
                              [URLs.HOMEPAGE, Locators.ORDER_FEED_BUTTON, "Лента заказов"]])
    def test_click_button(self, driver, url, button, header):
        click = BasePage(driver)

        click.go_to_page(url)
        click.click_visible_element(button)

        header_text = click.get_element_text(Locators.H1_HEADER)

        assert header_text == header

    @allure.title('Проверяем, что если кликнуть на ингредиент, появится всплывающее окно с деталями')
    def test_open_ingredient_modal(self, driver):
        ingredient = BasePage(driver)

        ingredient.go_to_page(URLs.HOMEPAGE)
        ingredient.click_visible_element(Locators.INGREDIENT)

        modal_header = ingredient.get_element_text(Locators.MODAL_HEADER)

        assert modal_header == 'Детали ингредиента'

    @allure.title('Проверяем, что всплывающее окно закрывается кликом по крестику')
    def test_close_modal(self, driver):
        modal = BasePage(driver)

        modal.go_to_page(URLs.HOMEPAGE)
        modal.click_visible_element(Locators.INGREDIENT)
        before_close_modal_class = modal.get_attribute_value(Locators.MODAL, 'class')

        modal.click_visible_element(Locators.MODAL_CLOSE)
        after_close_modal_class = modal.get_attribute_value(Locators.MODAL, 'class')

        assert 'opened' in before_close_modal_class
        assert 'opened' not in after_close_modal_class

    @allure.title('Проверяем, что при добавлении ингредиента в заказ счётчик этого ингредиента увеличивается')
    def test_ingredient_counter_increase(self, driver):
        move = BasePage(driver)

        move.go_to_page(URLs.HOMEPAGE)
        burger = move.find_visible_element(Locators.BURGER)
        ingredient = move.find_visible_element(Locators.INGREDIENT)
        counter_before = move.get_element_text(Locators.COUNTER)

        ActionChains(driver).drag_and_drop(ingredient, burger).perform()
        counter_after = move.get_element_text(Locators.COUNTER)

        assert counter_after > counter_before

    @allure.title('Проверяем, что залогиненный пользователь может оформить заказ.')
    def test_auth_user_create_order(self, driver, authorized_user):
        authorized_user.go_to_page(URLs.HOMEPAGE)

        burger = authorized_user.find_visible_element(Locators.BURGER)
        ingredient = authorized_user.find_visible_element(Locators.INGREDIENT)
        ActionChains(driver).drag_and_drop(ingredient, burger).perform()

        authorized_user.click_visible_element(Locators.ORDER_BUTTON)

        authorized_user.find_element_text_exclude(Locators.ORDER_NUMBER, '9999')
        order_number = int(authorized_user.get_element_text(Locators.ORDER_NUMBER))

        assert order_number > 0

