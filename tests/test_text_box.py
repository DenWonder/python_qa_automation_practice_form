from demoqa.data.simple_users import test_simple_user_1, test_simple_user_2
from demoqa.application import app

def test_text_box_page_object_patter(web_browser, text_box_page):
    text_box_page.fill_full_name(test_simple_user_1.full_name)
    text_box_page.fill_email(test_simple_user_1.email)
    text_box_page.fill_current_address(test_simple_user_1.current_address)
    text_box_page.fill_permanent_address(test_simple_user_1.permanent_address)
    text_box_page.submit()
    text_box_page.should_have_submitted(test_simple_user_1)

def test_text_box_page_object_with_assertion(web_browser, text_box_page):
    text_box_page.fill_full_name(test_simple_user_1.full_name)
    text_box_page.fill_email(test_simple_user_1.email)
    text_box_page.fill_current_address(test_simple_user_1.current_address)
    text_box_page.fill_permanent_address(test_simple_user_1.permanent_address)
    text_box_page.submit()
    assert text_box_page.get_output_values() == test_simple_user_1

def test_text_box_steps_object(web_browser, text_box_page):
    text_box_page.register_user(test_simple_user_2)
    text_box_page.should_have_submitted(test_simple_user_2)

def test_text_box_application_manager_pattern(web_browser):
    app.text_box_form.open()
    app.text_box_form.register_user(test_simple_user_2)
    app.text_box_form.should_have_submitted(test_simple_user_2)
