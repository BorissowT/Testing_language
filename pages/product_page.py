from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        self.should_be_add_to_basket()
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()

    def should_be_add_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), "there is no basket element"

    def should_be_name_product_in_alert(self):
        real_name = self.browser.find_element(*ProductPageLocators.PRODUCT_REAL_NAME)
        basket_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_FROM_ALERT)
        assert real_name.text == basket_name.text,\
            "names of product added to basket and real name aren't equal"

    def should_be_total_basket(self):
        real_price = self.browser.find_element(*ProductPageLocators.REAL_PRICE)
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE)
        assert real_price.text == basket_price.text, "real and basket price aren't equal"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message shouldn't be present"


