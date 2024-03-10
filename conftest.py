import pytest
from selenium import webdriver
import requests
import allure

from helper import valid_creds
from pages.account_page import AccountPage
from data import URLs, API, ingredients


@pytest.fixture(params=['chrome'])
def driver(request):
    driver = None
    if request.param == 'chrome':
        driver = webdriver.Chrome()
    elif request.param == 'firefox':    # по словам наставника, падение тестов в Firefox - ожидаемый результат
        driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.step('Регистрируем пользователя')
@pytest.fixture
def registered_user():
    creds = valid_creds()
    register = requests.post(API.USER_REGISTER, data=creds)
    user = {
        'creds': creds,
        'headers': {'Authorization': register.json()["accessToken"]}
    }
    yield user
    requests.delete(API.USER_DELETE, headers=user['headers'])


@allure.step('Открываем Личный кабинет пользователя')
@pytest.fixture
def authorized_user(registered_user, driver):
    authorized_user = AccountPage(driver)
    authorized_user.log_in(registered_user['creds'])
    authorized_user.go_to_page(URLs.ACCOUNT)

    return authorized_user


@allure.step('Авторизованный пользователь создал заказ')
@pytest.fixture
def auth_user_order(registered_user):
    headers = registered_user['headers']
    creds = registered_user['creds']

    order = requests.post(API.ORDERS, headers=headers, data=ingredients)
    number = order.json()['order']['number']
    auth_user_order = {'creds': creds, 'number': number}

    return auth_user_order
