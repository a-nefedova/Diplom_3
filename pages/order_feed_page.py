from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class OrderFeedPage(BasePage):

    def order_number_list(self, locator):
        order_list = WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located(locator))
        order_number_list = []
        for order in order_list:
            try:
                number = int(order.text[-5:])
                order_number_list.append(number)
            except Exception as e:
                if type(e) is ValueError:
                    return order_number_list
        return order_number_list

    def wait_order_in_list(self, number, locator):
        result = self.order_number_list(locator)
        while number not in result:
            result = self.order_number_list(locator)
        return result
