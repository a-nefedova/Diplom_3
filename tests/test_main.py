from pages.main_page import MainPage
from data import URLs
from locators.main_page_locators import LocatorsMain
import allure
from selenium.webdriver import ActionChains
import pytest


class TestMain:

    @allure.title('Проверяем переход по клику на кнопки «Конструктор» и «Лента заказов»')
    @allure.description('Используем параметризацию для кнопок')
    @pytest.mark.parametrize('url,button,header',
                             [[URLs.ORDER_FEED, LocatorsMain.CONSTRUCTOR_BUTTON, "Соберите бургер"],
                              [URLs.HOMEPAGE, LocatorsMain.ORDER_FEED_BUTTON, "Лента заказов"]])
    def test_click_button(self, driver, url, button, header):
        click = MainPage(driver)

        click.go_to_page(url)
        click.click_visible_element(button)

        header_text = click.get_element_text(LocatorsMain.H1_HEADER)

        assert header_text == header

    @allure.title('Проверяем, что если кликнуть на ингредиент, появится всплывающее окно с деталями')
    def test_open_ingredient_modal(self, driver):
        ingredient = MainPage(driver)

        ingredient.go_to_page(URLs.HOMEPAGE)
        ingredient.click_visible_element(LocatorsMain.INGREDIENT)

        details_presence = bool(ingredient.find_visible_element(LocatorsMain.DETAILS_MODAL))

        assert details_presence

    @allure.title('Проверяем, что всплывающее окно закрывается кликом по крестику')
    def test_close_modal(self, driver):
        modal = MainPage(driver)

        modal.go_to_page(URLs.HOMEPAGE)
        modal.click_visible_element(LocatorsMain.INGREDIENT)
        before_close_modal_class = modal.get_modal_class()

        modal.click_visible_element(LocatorsMain.MODAL_CLOSE)
        after_close_modal_class = modal.get_modal_class()

        assert 'opened' in before_close_modal_class
        assert 'opened' not in after_close_modal_class

    @allure.title('Проверяем, что при добавлении ингредиента в заказ счётчик этого ингредиента увеличивается')
    def test_ingredient_counter_increase(self, driver):
        move = MainPage(driver)

        move.go_to_page(URLs.HOMEPAGE)
        burger = move.find_visible_element(LocatorsMain.BURGER)
        ingredient = move.find_visible_element(LocatorsMain.INGREDIENT)

        counter_before = move.get_element_text(LocatorsMain.COUNTER)
        ActionChains(driver).drag_and_drop(ingredient, burger).perform()
        counter_after = move.get_element_text(LocatorsMain.COUNTER)

        assert counter_after > counter_before

    @allure.title('Проверяем, что залогиненный пользователь может оформить заказ.')
    def test_auth_user_create_order(self, driver, authorized_user):
        authorized_user.go_to_page(URLs.HOMEPAGE)

        burger = authorized_user.find_visible_element(LocatorsMain.BURGER)
        ingredient = authorized_user.find_visible_element(LocatorsMain.INGREDIENT)
        ActionChains(driver).drag_and_drop(ingredient, burger).perform()

        authorized_user.click_order_button()

        order_number = authorized_user.get_order_number(LocatorsMain.ORDER_NUMBER)

        assert order_number > 0
