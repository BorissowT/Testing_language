import time
import pytest
from .pages.main_page import MainPage
from .pages.basket_page import BasketPage
from .pages.product_page import ProductPage

link = "http://selenium1py.pythonanywhere.com/"


@pytest.mark.skip
def test_guest_can_go_to_login_page(browser):
    main_page = MainPage(browser, link)
    main_page.open()
    login_page = main_page.go_to_login_page()
    login_page.should_be_login_page()
    time.sleep(5)


@pytest.mark.skip
def test_guest_should_see_login_link(browser):
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/"
    main_page = MainPage(browser, link)
    main_page.open()
    main_page.go_to_basket()
    basket_page = BasketPage(browser, link)
    basket_page.should_be_empty()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-age-of-the-pussyfoot_89/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.go_to_basket()
    basket_page = BasketPage(browser, link)
    basket_page.should_be_empty()
