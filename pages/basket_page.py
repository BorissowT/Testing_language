from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty(self):
        self.should_be_out_of_products()
        self.should_show_empty_message()

    def should_show_empty_message(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_MESSAGE), "There is no message that basket is empty"

    def should_be_out_of_products(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCTS_BOX), \
            "There are products presented, but should not be"
