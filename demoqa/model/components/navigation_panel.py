from selene import have, command, be
from selene.support.shared import browser


class NavigationPanel:
    def __init__(self):
        self.container = browser.element('.left-pannel')

    def open(self, item):
        self.container.all('.menu-item').element_by(have.exact_text(item)).click()
        return self

    def open_text_box_form(self):
        self.container.open("Elements").open("Text Box")
        return self

    def open_practice_form(self):
        self.container.open("Forms").open("Practice Form")
        return self

    def open_book_store_login(self):
        self.container.open("Book Store Application").open("Login")
        return self

    def open_book_store(self):
        self.container.open("Book Store Application").open("Book Store")
        return self

    def open_book_store_profile(self):
        self.container.open("Book Store Application").open("Profile")
        return self