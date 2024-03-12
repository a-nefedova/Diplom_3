from pages.base_page import BasePage
from locators.main_page_locators import LocatorsMain


class MainPage(BasePage):

    def get_modal_class(self):
        return self.get_attribute_value(LocatorsMain.MODAL, 'class')
