from selene.support.shared import browser
from demoqa.endpoints import Endpoints


class BookStoreUserProfile:
    def __init__(self):
        self.user_name = browser.element('#userName-value')
        self.logout_button = browser. element("//button[text()='Logout']")
        self.go_to_book_store_button = browser.element('#gotoStore')
        self.delete_account_button = browser.element("//button[text()='Delete Account']")
        self.delete_all_books_button = browser.element('div.button.di').element('button')
        self.search_input = browser.element('#searchBox')
        self.search_button = browser.element('.btn.btn-outline-secondary')
        self.previous_button = browser.element('#')
        self.next_button = browser.element('#')

    def logout(self):
        self.logout_button.click()
        return self

    def go_to_book_store(self):
        self.go_to_book_store_button.click()
        return self

    def delete_account(self):
        self.delete_account_button.click()
        return self