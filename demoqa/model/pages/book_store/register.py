from selene.support.shared import browser
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils import constants

from demoqa.data.book_store_user import BookStoreUser
from demoqa.endpoints import Endpoints


class RegisterPage:
    first_name_input_field = browser.element('#firstname')
    last_name_input_field = browser.element('#lastname')
    user_name_input_field = browser.element('#userName')
    password_input_field = browser.element('#password')
    register_button = browser.element('#register')
    back_to_login_button = browser.element('#gotologin')

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

    def fill_password(self, value):
        self.password_input_field.type(value)
        return self

    def click_register(self):
        self.register_button.click()
        return self

    def click_back_to_login(self):
        self.back_to_login_button.click()
        return self

    def get_alert_message(self):
        WebDriverWait(browser.driver, 10).until(EC.alert_is_present())
        message = browser.switch_to.alert.text
        return message

    def accept_alert_message(self):
        browser.switch_to.alert.accept()

    #endregion

    #region StepObject pattern methods

    def register(self, user_data: BookStoreUser):
        self.fill_first_name(user_data.first_name)
        self.fill_last_name(user_data.last_name)
        self.fill_user_name(user_data.user_name)
        self.fill_password(user_data.password)
        self.click_register()
        return self

    def is_registration_successfully(self):
        message = self.get_alert_message()
        self.accept_alert_message()
        return message == constants.USER_REGISTERED_SUCCESSFULLY_MESSAGE

    #endregion
