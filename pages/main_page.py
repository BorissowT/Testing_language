from .base_page import BasePage


class MainPage(BasePage):
    ##instance of BaseP object with args
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)
