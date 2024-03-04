import pytest
from selenium import webdriver
import requests

from pages.base_page import BasePage
from data import URLs, API
from locators import Locators


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def registered_user():

    creds = BasePage.valid_creds()
    register = requests.post(API.USER_REGISTER, data=creds)

    user = {
        'creds': creds,
        'headers': {'Authorization': register.json()["accessToken"]}
    }

    yield user

    requests.delete(API.USER_DELETE, headers=user['headers'])


@pytest.fixture
def authorized_user(registered_user, driver):
    authorized_user = BasePage(driver)

    authorized_user.go_to_page(URLs.LOGIN)
    authorized_user.log_in(registered_user['creds'])
    authorized_user.find_visible_element(Locators.ORDER_BUTTON)
    authorized_user.go_to_page(URLs.ACCOUNT)

    return authorized_user
