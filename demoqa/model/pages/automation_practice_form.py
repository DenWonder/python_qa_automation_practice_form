from selene import have, command, be
from selene.support.shared import browser

from demoqa.data.users import User
from tests.endpoints import Endpoints


class AutomationPracticeForm:
    def __init__(self):
        self.first_name_input_field = browser.element('#firstName')
        self.last_name_input_field = browser.element('#lastName')
        self.email_input_field = browser.element('#userEmail')
        self.gender_wrapper_radio_buttons = browser.element('#genterWrapper').all('.form-check')
        self.mobile_input_field = browser.element('#userNumber')
        self.date_of_birth_input_field = browser.element('#dateOfBirthInput')
        self.subjects_input_field = browser.element('#subjectsInput')
        self.hobbies_wrapper_checkboxes = browser.element('#hobbiesWrapper').all('.form-check')
        self.picture_input_field = browser.element('#uploadPicture')
        self.current_address_input_field = browser.element('#currentAddress')
        self.state_dropdown = browser.element('#state')
        self.city_dropdown = browser.element('#city')
        self.submit_button = browser.element('#submit')
        self.close_modal_button = browser.element('#closeLargeModal')

    def open(self):
        browser.open(Endpoints.AUTOMATION_PRACTICE_FORM_URL)
        return self

    def fill_first_name(self, value):
        self.first_name_input_field.type(value)
        return self

    def fill_last_name(self, value):
        self.last_name_input_field.type(value)
        return self

    def fill_email(self, value):
        self.email_input_field.type(value)
        return self

    def select_gender(self, gender: str):
        self.gender_wrapper_radio_buttons.element_by(have.exact_text(gender.capitalize())).click()
        return self

    def fill_mobile(self, value):
        self.mobile_input_field.type(value)
        return self

    def fill_date_of_birth(self, year, month, day):
        self.date_of_birth_input_field.click()
        browser.element('.react-datepicker__year-select').all('option') \
            .element_by(have.exact_text(str(year))).click()
        browser.element('.react-datepicker__month-select').all('option') \
            .element_by(have.exact_text(f"{month}")).click()
        browser.element(f'.react-datepicker__day--0{day}').click()
        return self

    def fill_subjects(self, values):
        for value in values:
            self.subjects_input_field.click()
            self.subjects_input_field.type(f"{value}").press_enter()
        return self

    def select_hobbies(self, hobbies):
        for hobby in hobbies:
            self.hobbies_wrapper_checkboxes.element_by(have.exact_text(hobby)).click()
        return self

    def fill_picture(self, value):
        self.picture_input_field.set_value(value)
        return self

    def fill_current_address(self, value):
        self.current_address_input_field.set_value(value)
        return self

    def select_state(self, state):
        self.state_dropdown.click()
        states = browser.element('#react-select-3-listbox')
        states.all('div[role="option"]').element_by(have.exact_text(state)).click()
        return self

    def select_city(self, city):
        self.city_dropdown.click()
        cities = browser.element('#react-select-4-listbox')
        cities.all('div[role="option"]').element_by(have.exact_text(city)).click()
        return self

    def submit(self):
        self.submit_button.click()
        return self

    def should_registered_user_with(self, first_name, last_name, email, gender,
                                    phone_number, birth_year, birth_month, birth_day,
                                    subjects, hobbies, upload_filename,
                                    current_address, state, city
                                    ):
        full_name = first_name + " " + last_name
        full_birthday = f"{birth_day} {birth_month},{birth_year}"
        state_and_city = state + " " + city
        browser.element('.table').all('td').even.should(
            have.exact_texts(
                full_name,
                email,
                gender,
                f'{phone_number}',
                full_birthday,
                subjects,
                hobbies,
                upload_filename,
                current_address,
                state_and_city
            )
        )
        self.close_modal_button.should(be.clickable)
        return self

    def should_contain_registered_user_data(self, user: User):
        full_name = user.first_name + " " + user.last_name
        full_birthday = f"{user.birth_day} {user.birth_month},{user.birth_year}"
        state_and_city = user.state + " " + user.city
        subjects_line = ", ".join(str(item) for item in user.subjects)
        hobbies_line = ", ".join(str(item) for item in user.hobbies)
        browser.element('.table').all('td').even.should(
            have.exact_texts(
                full_name,
                user.email,
                user.gender,
                user.phone_number,
                full_birthday,
                subjects_line,
                hobbies_line,
                user.picture,
                user.current_address,
                state_and_city
            )
        )
        self.close_modal_button.should(be.clickable)
        return self


