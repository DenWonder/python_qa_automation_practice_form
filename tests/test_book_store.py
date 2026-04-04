from time import sleep

from demoqa.application import app
from demoqa.data.book_store_user import test_book_store_user_1, test_book_store_user_2

def test_book_store_registration(web_browser, book_store_registration):
    sleep(5)
    book_store_registration.fill_first_name(test_book_store_user_1.first_name)
    book_store_registration.fill_last_name(test_book_store_user_1.last_name)
    book_store_registration.fill_user_name(test_book_store_user_1.user_name)
    book_store_registration.fill_password_value(test_book_store_user_1.password)
    book_store_registration.click_register_button()
    sleep(5)
    assert book_store_registration.get_alert_message() == "User Registered Successfully."
    book_store_registration.accept_alert_message()
