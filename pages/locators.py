from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    EMAIL_REGISTRATION_INPUT = (By.CSS_SELECTOR, "input#id_registration-email")
    PASS_1_REGISTRATION_INPUT = (By.CSS_SELECTOR, "input#id_registration-password1")
    PASS_2_REGISTRATION_INPUT = (By.CSS_SELECTOR, "input#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "[name~='registration_submit']")


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_REAL_NAME = (By.CSS_SELECTOR, "h1:first-child")
    PRODUCT_NAME_FROM_ALERT = (By.CSS_SELECTOR, ".alert:first-child > .alertinner > strong")
    REAL_PRICE = (By.CSS_SELECTOR, ".product_main > .price_color")
    BASKET_PRICE = (By.CSS_SELECTOR, ".alert > .alertinner >p > strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert > .alertinner")


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-group > a")
    USER_ICON = (By.ID, "logout_link")


class BasketPageLocators:
    PRODUCTS_BOX = (By.CSS_SELECTOR, ".basket-title")
    EMPTY_MESSAGE = (By.CSS_SELECTOR, "#content_inner > p")