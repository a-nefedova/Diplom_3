from selenium.webdriver.common.by import By


class Locators:

    FORGOT_PASS_LINK = (By.XPATH, './/a[@href="/forgot-password"]')
    H1_HEADER = (By.XPATH, './/main//h1')
    H2_HEADER = (By.XPATH, './/main//h2')

    EMAIL_INPUT = (By.XPATH, './/form//label[text()="Email"]/parent::*/input')
    RESET_BUTTON = (By.XPATH, './/form//button[text()="Восстановить"]')

    PASS_INPUT = (By.CLASS_NAME, 'input_type_password')
    PASS_PLACEHOLDER = (By.XPATH, './/form//label[text()="Пароль"]')
    NOT_PASS_PLACEHOLDER = (By.XPATH, './/form//label[not(text()="Пароль")]')
    SHOW_PASS_BUTTON = (By.XPATH, './/form//label[text()="Пароль"]//following::*[local-name()="svg"]')

    LOGIN_BUTTON = (By.XPATH, './/button[text()="Войти"]')  # кнопка "Войти" в форме логина
    EMAIL = (By.XPATH, './/form//label[text()="Email"]/parent::*/input')  # поле для ввода email при регистрации
    PASSWORD = (By.XPATH, './/input[@type="password"]')  # поле для ввода пароля при регистрации
    LOGOUT_BUTTON = (By.XPATH, './/button[text()="Выход"]')

    ORDER_BUTTON = (By.XPATH, './/button[text()="Оформить заказ"]')  # кнопка "Оформить заказ"

    ACCOUNT_LINK = (By.XPATH, './/a[@href="/account"]')  # ссылка на Личный кабинет
    ACCOUNT_EMAIL = (By.XPATH,  # поле с тестовым email в Личном кабинете
                     f'.//label[text()="Логин"]/parent::div/input[@value]')

    ORDER_HISTORY_BUTTON = (By.XPATH, './/a[@href="/account/order-history"]')

    CONSTRUCTOR_BUTTON = (By.XPATH, './/p[text()="Конструктор"]/parent::a')
    ORDER_FEED_BUTTON = (By.XPATH, './/p[text()="Лента Заказов"]/parent::a')

    INGREDIENT = (By.XPATH, './/div[contains(@class,"menu")]//p[text()="Флюоресцентная булка R2-D3"]')
    COUNTER = (By.XPATH, f'{INGREDIENT[1]}/preceding::p[contains(@class,"counter__num")]')
    MODAL = (By.XPATH, './/h2[text()="Детали ингредиента"]/ancestor::section')
    MODAL_HEADER = (By.XPATH, './/section[contains(@class,"modal_opened")]//h2')
    MODAL_CLOSE = (By.XPATH, './/section[contains(@class,"modal_opened")]//button[contains(@class,"modal__close")]')

    BURGER = (By.XPATH, './/section[contains(@class,"basket")]')

    ORDER_NUMBER = (By.XPATH, './/p[text()="идентификатор заказа"]/preceding-sibling::h2')



