from data import URLs
from locators.order_feed_page_locators import LocatorsOrder
from pages.order_feed_page import OrderFeedPage
from helper import create_order
import allure
import pytest


class TestOrderFeed:

    @allure.title('Проверяем, что если кликнуть на заказ, откроется всплывающее окно с деталями')
    def test_open_order_modal(self, driver):
        order = OrderFeedPage(driver)

        order.go_to_page(URLs.ORDER_FEED)
        order.click_visible_element(LocatorsOrder.ORDER_FEED_LIST)
        details_presence = bool(order.find_visible_element(LocatorsOrder.ORDER_DETAILS))

        assert details_presence

    @allure.title('Проверяем, что заказы пользователя из раздела «История заказов» отображаются '
                  'на странице «Лента заказов»')
    def test_user_order_in_order_feed(self, driver, authorized_user, auth_user_order):
        order = OrderFeedPage(driver)

        authorized_user.click_order_history_button()
        user_order_number = authorized_user.get_order_history_number()

        order.go_to_page(URLs.ORDER_FEED)
        order_list = order.wait_order_in_list(user_order_number, LocatorsOrder.ORDER_FEED_LIST)

        assert user_order_number in order_list

    @pytest.mark.parametrize('locator', [LocatorsOrder.ALL_TIME_ORDERS, LocatorsOrder.TODAY_ORDERS])
    @allure.title('Проверяем, что при создании нового заказа '
                  'счётчики "Выполнено за всё время" и "Выполнено за сегодня" увеличиваются')
    @allure.description('Используем параметризацию для счётчиков')
    def test_order_counter_increase(self, driver, registered_user, locator):
        counter = OrderFeedPage(driver)

        counter.go_to_page(URLs.ORDER_FEED)
        counter_before = int(counter.get_element_text(locator))
        number = create_order(registered_user['headers'])
        counter.wait_order_in_list(number, LocatorsOrder.ORDER_FEED_LIST)
        counter_after = int(counter.get_element_text(locator))

        assert counter_after > counter_before
        # Этот тест иногда падает из-за того, что счётчик иногда вычитает 1, как будто кто-то удаляет заказ.
        # Не додумалась, как обойти этот баг.

    @allure.title('Проверяем, что после оформления заказа его номер появляется в разделе В работе')
    def test_order_in_progress(self, driver, registered_user):
        progress = OrderFeedPage(driver)

        progress.go_to_page(URLs.ORDER_FEED)

        number = create_order(registered_user['headers'])
        order_in_progress = progress.wait_order_in_list(number, LocatorsOrder.ORDER_IN_PROGRESS)

        assert number in order_in_progress
