from selene.support.shared import browser

from demoqa.data.book_store_user import BookStoreUser
from demoqa.endpoints import Endpoints


class LoginPage:
    def __init__(self):
        self.user_name_input_field = browser.element("#userName")
        self.password_input_field = browser.element("#password")
        self.login_button = browser.element("#login")
        self.new_user_button = browser.element("#newUser")

    def open(self):
        browser.open(Endpoints.BOOK_STORE_LOGIN_URL)
        return self

    #region classic PageObject pattern methods

    def fill_user_name(self, value):
        self.user_name_input_field.type(value)
        return self

    def fill_password(self, value):
        self.password_input_field.type(value)
        return self

    def click_login(self):
        self.login_button.click()
        return self

    def click_new_user(self):
        self.new_user_button.click()
        return self

    #endregion

    #region StepObject pattern methods

    def login(self, user_data: BookStoreUser):
        self.fill_user_name(user_data.user_name)
        self.fill_password(user_data.password)
        self.click_login()
        return self

    #endregion