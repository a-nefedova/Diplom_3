import requests
from pages.login_page import LoginPage
from data import URLs, API, ingredients
from locators import Locators
import allure
import pytest


class TestOrderFeed:

    @allure.title('Проверяем, что если кликнуть на заказ, откроется всплывающее окно с деталями')
    def test_open_order_modal(self, driver):
        order = LoginPage(driver)

        order.go_to_page(URLs.ORDER_FEED)
        order.click_visible_element(Locators.ORDER_FEED_LIST)

        details_presence = bool(order.find_visible_elements(Locators.ORDER_DETAILS))

        assert details_presence

    @allure.title('Проверяем, что заказы пользователя из раздела «История заказов» отображаются '
                  'на странице «Лента заказов»')
    def test_user_order_in_order_feed(self, driver, auth_user_order):
        creds = auth_user_order['creds']
        order = LoginPage(driver)

        order.log_in(creds)
        order.go_to_page(URLs.ACCOUNT)
        order.click_visible_element(Locators.ORDER_HISTORY_BUTTON)
        raw_order_number = order.get_element_text(Locators.ORDER_NUMBER_HISTORY)
        order_number = int(raw_order_number[-5:])

        order.go_to_page(URLs.ORDER_FEED)
        order_list = order.order_number_list(Locators.ORDER_FEED_LIST)

        assert order_number in order_list

    @pytest.mark.parametrize('locator', [Locators.ALL_TIME_ORDERS, Locators.TODAY_ORDERS])
    @allure.title('Проверяем, что при создании нового заказа счётчик Выполнено за всё время увеличивается')
    def test_order_counter_increase(self, driver, registered_user, locator):
        counter = LoginPage(driver)

        counter.go_to_page(URLs.ORDER_FEED)
        counter_before = int(counter.get_element_text(locator))

        order = requests.post(API.ORDERS, headers=registered_user['headers'], data=ingredients)
        number = order.json()['order']['number']
        while number not in counter.order_number_list(Locators.ORDER_FEED_LIST):
            continue
        counter_after = int(counter.get_element_text(locator))

        assert counter_after > counter_before
        # Этот тест иногда падает из-за того, что счётчик иногда вычитает 1, как будто кто-то удаляет заказ.
        # Не додумалась, как обойти этот баг.

    @allure.title('Проверяем, что после оформления заказа его номер появляется в разделе В работе')
    def test_order_in_progress(self, driver, registered_user):
        progress = LoginPage(driver)

        progress.go_to_page(URLs.ORDER_FEED)

        order = requests.post(API.ORDERS, headers=registered_user['headers'], data=ingredients)
        number = order.json()['order']['number']
        while number not in progress.order_number_list(Locators.ORDER_IN_PROGRESS):
            continue
        else:
            order_in_progress = progress.order_number_list(Locators.ORDER_IN_PROGRESS)

        assert number in order_in_progress
