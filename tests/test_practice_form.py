from demoqa.data.users import test_user_1, test_user_2
from demoqa.application import app
import allure

"""
    This file contains three tests that are functionally identical but implemented using three different approaches. 
"""
@allure.feature("Registration form")
@allure.story("Smoke test")
@allure.label("Owner", "Den Wonder")
def test_practice_form_page_object_pattern(web_browser, practice_form_page):
    practice_form_page.fill_first_name(test_user_1.first_name)
    practice_form_page.fill_last_name(test_user_1.last_name)
    practice_form_page.fill_email(test_user_1.email)
    practice_form_page.select_gender(test_user_1.gender)
    practice_form_page.fill_mobile(test_user_1.phone_number)
    practice_form_page.fill_date_of_birth(test_user_1.birth_year, test_user_1.birth_month, test_user_1.birth_day)
    practice_form_page.fill_subjects(test_user_1.subjects)
    practice_form_page.select_hobbies(test_user_1.hobbies)
    practice_form_page.fill_picture(test_user_1.picture)
    practice_form_page.fill_current_address(test_user_1.current_address)
    practice_form_page.select_state(test_user_1.state)
    practice_form_page.select_city(test_user_1.city)
    practice_form_page.submit()
    practice_form_page.should_contain_registered_user_data(test_user_1)

@allure.feature("Registration form")
@allure.story("Smoke test")
@allure.label("Owner", "Den Wonder")
def test_practice_form_steps_object_pattern(web_browser, practice_form_page):
    practice_form_page.register_user(test_user_2)
    practice_form_page.should_contain_registered_user_data(test_user_2)

@allure.feature("Registration form")
@allure.story("Smoke test")
@allure.label("Owner", "Den Wonder")
def test_practice_form_application_manager_and_steps_object_pattern(web_browser):
    """
        Application Manager pattern approach: (aka Single Entry Point)
        A single App class serves as the entry point to all page objects.
        This avoids scattered "page = Page()" calls in every test, keeps page
        object wiring in one place, and makes the test API discoverable through IDE autocompletion on app.
    """
    app.practice_form.open()
    app.practice_form.register_user(test_user_1)
    app.practice_form.should_contain_registered_user_data(test_user_1)
