from selenium.webdriver.common.by import By


class Locators:

    FORGOT_PASS_LINK = (By.XPATH, './/a[@href="/forgot-password"]')
    H1_HEADER = (By.XPATH, './/main//h1')
    H2_HEADER = (By.XPATH, './/main//h2')

    EMAIL_INPUT = (By.XPATH, './/form//label[text()="Email"]/parent::*/input')
    RESET_BUTTON = (By.XPATH, './/form//button[text()="Восстановить"]')

    PASS_INPUT = (By.XPATH, './/div[contains(@class,"input_type_password")]')
    PASS_PLACEHOLDER = (By.XPATH, './/form//label[text()="Пароль"]')
    ENTER_CODE_PLACEHOLDER = (By.XPATH, './/form//label[not(text()="Пароль")]')
    SHOW_PASS_BUTTON = (By.XPATH, './/form//label[text()="Пароль"]//following::*[local-name()="svg"]')

    LOGIN_BUTTON = (By.XPATH, './/button[text()="Войти"]')
    EMAIL = (By.XPATH, './/form//label[text()="Email"]/parent::*/input')
    PASSWORD = (By.XPATH, './/input[@type="password"]')
    LOGOUT_BUTTON = (By.XPATH, './/button[text()="Выход"]')

    ORDER_BUTTON = (By.XPATH, './/button[text()="Оформить заказ"]')

    ACCOUNT_LINK = (By.XPATH, './/a[@href="/account"]')
    ACCOUNT_EMAIL = (By.XPATH, './/label[text()="Логин"]/parent::div/input[@value]')

    ORDER_HISTORY_BUTTON = (By.XPATH, './/a[@href="/account/order-history"]')
    ORDER_NUMBER_HISTORY = (By.XPATH, './/div[contains(@class,"orderHistory")]//p[contains(text(),"#")]')

    CONSTRUCTOR_BUTTON = (By.XPATH, './/p[text()="Конструктор"]/parent::a')
    ORDER_FEED_BUTTON = (By.XPATH, './/p[text()="Лента Заказов"]/parent::a')
    ORDER_FEED_LIST = (By.XPATH, './/ul[contains(@class,"OrderFeed_list")]//p[contains(text(),"#")]')
    ORDER_DETAILS = (By.XPATH, './/section[contains(@class,"modal_opened")]//ul/li')
    ALL_TIME_ORDERS = (By.XPATH, './/p[text()="Выполнено за все время:"]/'
                                 'following::p[contains(@class,"OrderFeed_number")]')
    TODAY_ORDERS = (By.XPATH, './/p[text()="Выполнено за сегодня:"]/following::p[contains(@class,"OrderFeed_number")]')
    ORDER_IN_PROGRESS = (By.XPATH, './/ul[contains(@class,"OrderFeed_orderListReady")]/li')

    INGREDIENT = (By.XPATH, './/div[contains(@class,"menu")]//p[text()="Флюоресцентная булка R2-D3"]')
    COUNTER = (By.XPATH, f'{INGREDIENT[1]}/preceding::p[contains(@class,"counter__num")]')
    MODAL = (By.XPATH, './/h2[text()="Детали ингредиента"]/ancestor::section')
    MODAL_HEADER = (By.XPATH, './/section[contains(@class,"modal_opened")]//h2')
    MODAL_CLOSE = (By.XPATH, './/section[contains(@class,"modal_opened")]//button[contains(@class,"modal__close")]')

    BURGER = (By.XPATH, './/section[contains(@class,"basket")]')

    ORDER_NUMBER = (By.XPATH, './/p[text()="идентификатор заказа"]/preceding-sibling::h2')



