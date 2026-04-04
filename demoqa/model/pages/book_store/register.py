from selene.support.shared import browser

from demoqa.data.book_store_user import BookStoreUser
from demoqa.endpoints import Endpoints


class RegisterPage:
    def __init__(self):
        self.first_name_input_field = browser.element('#firstname')
        self.last_name_input_field = browser.element('#lastname')
        self.user_name_input_field = browser.element('#userName')
        self.password_input_field = browser.element('#password')
        self.register_button = browser.element('#register')
        self.back_to_login_button = browser.element('#gotologin')

    def open(self):
        browser.open(Endpoints.BOOK_STORE_REGISTER_URL)
        return self

    #region classic PageObject pattern methods

    def fill_first_name(self, value):
        self.first_name_input_field.type(value)
        return self

    def fill_last_name(self, value):
        self.last_name_input_field.type(value)
        return self

    def fill_user_name(self, value):
        self.user_name_input_field.type(value)
        return self

    def fill_password_value(self, value):
        self.password_input_field.type(value)
        return self

    def click_register_button(self):
        self.register_button.click()
        return self

    def click_back_to_login_button(self):
        self.back_to_login_button.click()
        return self

    #endregion

    #region StepObject pattern methods

    def register(self, user_data: BookStoreUser):
        self.fill_first_name(user_data.first_name)
        self.fill_last_name(user_data.last_name)
        self.fill_user_name(user_data.user_name)
        self.fill_password_value(user_data.password)
        return self

    #endregion