import time
from .pages.main_page import MainPage

link = "http://selenium1py.pythonanywhere.com/"


def test_guest_can_go_to_login_page(browser):
    main_page = MainPage(browser, link)
    main_page.open()
    login_page = main_page.go_to_login_page()
    login_page.should_be_login_page()
    time.sleep(5)


def test_guest_should_see_login_link(browser):
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()

