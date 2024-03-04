import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    @allure.step('Открываем браузер')
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Переходим на страницу')
    def go_to_page(self, url):
        self.driver.get(url)

    def find_visible_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator))

    def click_visible_element(self, locator, time=10):
        self.find_visible_element(locator, time).click()

    def get_element_text(self, locator):
        return self.find_visible_element(locator).text

    def wait_until_url_change(self, url):
        WebDriverWait(self.driver, 5).until(EC.url_changes(url))
