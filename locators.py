from selenium.webdriver.common.by import By


class Locators:

    FORGOT_PASS_LINK = (By.XPATH, './/a[@href="/forgot-password"]')
    H2_HEADER = (By.XPATH, './/main//h2')

    EMAIL_INPUT = (By.XPATH, './/form//label[text()="Email"]/parent::*/input')
    RESET_BUTTON = (By.XPATH, './/form//button[text()="Восстановить"]')

    PASS_INPUT = (By.CLASS_NAME, 'input_type_password')
    PASS_PLACEHOLDER = (By.XPATH, './/form//label[text()="Пароль"]')
    NOT_PASS_PLACEHOLDER = (By.XPATH, './/form//label[not(text()="Пароль")]')
    SHOW_PASS_BUTTON = (By.XPATH, './/form//label[text()="Пароль"]//following::*[local-name()="svg"]')



