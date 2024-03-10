from selenium.webdriver.common.by import By


class LocatorsAccount:
    LOGIN_BUTTON = (By.XPATH, './/button[text()="Войти"]')
    EMAIL = (By.XPATH, './/form//label[text()="Email"]/parent::*/input')
    PASSWORD = (By.XPATH, './/input[@type="password"]')
    LOGOUT_BUTTON = (By.XPATH, './/button[text()="Выход"]')

    ORDER_BUTTON = (By.XPATH, './/button[text()="Оформить заказ"]')

    ACCOUNT_LINK = (By.XPATH, './/a[@href="/account"]')
    ACCOUNT_EMAIL = (By.XPATH, './/label[text()="Логин"]/parent::div/input[@value]')

    ORDER_HISTORY_BUTTON = (By.XPATH, './/a[@href="/account/order-history"]')
    ORDER_NUMBER_HISTORY = (By.XPATH, './/div[contains(@class,"orderHistory")]//p[contains(text(),"#")]')
