from operator import contains

from selene.support.shared import browser
from selene import have, be, query

from demoqa.data.simple_users import SimpleUser
from demoqa.endpoints import Endpoints


class TextBoxForm:
    def __init__(self):
        self.full_name_input_field = browser.element('#userName')
        self.email_input_field = browser.element('#userEmail')
        self.current_address_input_field = browser.element('#currentAddress')
        self.permanent_address_input_field = browser.element('#permanentAddress')
        self.submit_button = browser.element('#submit')
        self.output = browser.element('#output')
        self.output_name = self.output.element('#name')
        self.output_email = self.output.element('#email')
        self.output_current_address = self.output.element('#currentAddress')
        self.output_permanent_address = self.output.element('#permanentAddress')

    def open(self):
        browser.open(Endpoints.TEXT_BOX_URL)
        return self

    def _type_if_present(self, element, value):
        if value:
            element.type(value)
        return self

    #region classic PageObject pattern methods

    def fill_full_name(self, value):
        return self._type_if_present(self.full_name_input_field, value)

    def fill_email(self, value):
        return self._type_if_present(self.email_input_field, value)

    def fill_permanent_address(self, value):
        return self._type_if_present(self.permanent_address_input_field, value)

    def fill_current_address(self, value):
        return self._type_if_present(self.current_address_input_field, value)

    def submit(self):
        self.submit_button.click()
        return self

    #endregion

    #region Steps object pattern methods

    def register_user(self, user_data: SimpleUser):
        self.fill_full_name(user_data.full_name)
        self.fill_email(user_data.email)
        self.fill_permanent_address(user_data.permanent_address)
        self.fill_current_address(user_data.current_address)
        self.submit()
        return self

    #endregion

    def should_have_submitted(self, user_data: SimpleUser):

        self.output_name.should(have.text(user_data.full_name))
        self.output_email.should(have.text(user_data.email))
        if user_data.current_address:
            self.output_current_address.should(have.text(user_data.current_address))
        if user_data.permanent_address:
            self.output_permanent_address.should(have.text(user_data.permanent_address))

    def _get_text_or_none(self, element) -> str | None:
        try:
            element.should(be.visible)
            return element.get(query.text).split(":", 1)[1].strip()
        except Exception:
            return None

    def get_output_values(self):
        return SimpleUser(
            full_name=self._get_text_or_none(self.output_name),
            email=self._get_text_or_none(self.output_email),
            current_address=self._get_text_or_none(self.output_current_address),
            permanent_address=self._get_text_or_none(self.output_permanent_address),
        )