import os.path
from time import sleep
from selene import browser, have

from demoqa.data.users import test_user_1
from demoqa.model.pages.automation_practice_form import AutomationPracticeForm
from tests.endpoints import Endpoints


def test_practice_form_with_pattern(browser_config):
    practice_form = AutomationPracticeForm()
    practice_form.open()
    practice_form.fill_first_name(test_user_1.first_name)
    practice_form.fill_last_name(test_user_1.last_name)
    practice_form.fill_email(test_user_1.email)
    practice_form.select_gender(test_user_1.gender)
    practice_form.fill_mobile(test_user_1.phone_number)
    practice_form.fill_date_of_birth(test_user_1.birth_year, test_user_1.birth_month, test_user_1.birth_day)
    practice_form.fill_subjects(test_user_1.subjects)
    practice_form.select_hobbies(test_user_1.hobbies)
    practice_form.fill_picture(os.path.join(os.path.dirname(os.path.abspath(__file__)), "resources", test_user_1.picture))
    practice_form.fill_current_address(test_user_1.current_address)
    practice_form.select_state(test_user_1.state)
    practice_form.select_city(test_user_1.city)
    practice_form.submit()
    sleep(3)
    practice_form.should_contain_registered_user_data(test_user_1)


