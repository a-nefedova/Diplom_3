from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class OrderFeedPage(BasePage):

    def order_number_list(self, locator):
        order_list = WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located(locator))
        order_number_list = []
        number = None
        for order in order_list:
            try:
                number = int(order.text[-5:])
            except Exception as e:
                if type(e) is ValueError:
                    return order_number_list
            order_number_list.append(number)
        return order_number_list

    def wait_order_in_list(self, number, locator):
        while number not in self.order_number_list(locator):
            continue
        else:
            return self.order_number_list(locator)
