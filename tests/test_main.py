from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from data import URLs
from locators import Locators
import allure

from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains


class TestMain:

    def test_open_constructor(self, driver):
        constructor = BasePage(driver)

        constructor.go_to_page(URLs.ORDER_FEED)
        constructor.click_visible_element(Locators.CONSTRUCTOR_BUTTON)

        constructor_header = constructor.get_element_text(Locators.H1_HEADER)

        assert constructor_header == "Соберите бургер"

    def test_open_order_feed(self, driver):
        order_feed = BasePage(driver)

        order_feed.go_to_page(URLs.HOMEPAGE)
        order_feed.click_visible_element(Locators.ORDER_FEED_BUTTON)

        order_feed_header = order_feed.get_element_text(Locators.H1_HEADER)

        assert order_feed_header == "Лента заказов"

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
        before_close_modal_class = modal.find_visible_element(Locators.MODAL).get_attribute("class")

        modal.click_visible_element(Locators.MODAL_CLOSE)
        after_close_modal_class = modal.find_visible_element(Locators.MODAL).get_attribute("class")

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

