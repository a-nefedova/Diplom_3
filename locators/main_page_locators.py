from selenium.webdriver.common.by import By


class LocatorsMain:
    H1_HEADER = (By.XPATH, './/main//h1')
    CONSTRUCTOR_BUTTON = (By.XPATH, './/p[text()="Конструктор"]/parent::a')
    ORDER_FEED_BUTTON = (By.XPATH, './/p[text()="Лента Заказов"]/parent::a')
    INGREDIENT = (By.XPATH, './/div[contains(@class,"menu")]//p[text()="Флюоресцентная булка R2-D3"]')
    COUNTER = (By.XPATH, f'{INGREDIENT[1]}/preceding::p[contains(@class,"counter__num")]')
    MODAL = (By.XPATH, './/h2[text()="Детали ингредиента"]/ancestor::section')
    DETAILS_MODAL = (By.XPATH, './/section[contains(@class,"modal_opened")]//*[text()="Детали ингредиента"]')
    MODAL_CLOSE = (By.XPATH, './/section[contains(@class,"modal_opened")]//button[contains(@class,"modal__close")]')

    BURGER = (By.XPATH, './/section[contains(@class,"basket")]')

    ORDER_NUMBER = (By.XPATH, './/p[text()="идентификатор заказа"]/preceding-sibling::h2')
