import time

from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "page isn't a login page"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        email_registration = self.browser.find_element(*LoginPageLocators.EMAIL_REGISTRATION_INPUT)
        email_registration.send_keys(str(email))
        first_pass = self.browser.find_element(*LoginPageLocators.PASS_1_REGISTRATION_INPUT)
        first_pass.send_keys(str(password))
        second_pass = self.browser.find_element(*LoginPageLocators.PASS_2_REGISTRATION_INPUT)
        second_pass.send_keys(str(password))
        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        register_button.click()
