from selene.support.shared import browser

from demoqa.data.simple_users import SimpleUser
from demoqa.endpoints import Endpoints


class TextBoxForm:
    def __init__(self):
        self.full_name_input_field = browser.element('#userName')
        self.email_input_field = browser.element('#userEmail')
        self.current_address_input_field = browser.element('#currentAddress')
        self.permanent_address_input_field = browser.element('#permanentAddress')
        self.submit_button = browser.element('#submit')

    def open(self):
        browser.open(Endpoints.TEXT_BOX_URL)
        return self

    #regiion classic PageObject pattern methods

    def fill_full_name(self, value):
        self.full_name_input_field.fill(value)
        return self

    def fill_email(self, value):
        self.email_input_field.fill(value)
        return self

    def fill_permanent_address(self, value):
        self.permanent_address_input_field.fill(value)
        return self

    def fill_current_address(self, value):
        self.current_address_input_field.fill(value)
        return self

    def submit(self):
        self.submit_button.click()
        return self

    #endregion

    #region Steps object pattern methods

    def register_user(self, user_data: SimpleUser):
        return self

    #endregion