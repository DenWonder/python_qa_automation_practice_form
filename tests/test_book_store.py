from demoqa.application import app
from utils import constants
from demoqa.data.book_store_user import test_book_store_user_1, test_book_store_user_2

def test_book_store_registration(web_browser, book_store_registration):
    """
        Classic Page Object pattern.
        Показывает техническую реализацию пошагово —
        каждое действие явно вызывается в теле теста.
    """
    book_store_registration.fill_first_name(test_book_store_user_1.first_name)
    book_store_registration.fill_last_name(test_book_store_user_1.last_name)
    book_store_registration.fill_user_name(test_book_store_user_1.user_name)
    book_store_registration.fill_password(test_book_store_user_1.password)
    book_store_registration.click_register()
    assert book_store_registration.get_alert_message() == constants.USER_REGISTERED_SUCCESSFULLY_MESSAGE
    book_store_registration.accept_alert_message()

def test_book_store_registration_step_object(web_browser, book_store_registration):
    """
        Step Object pattern.
        Скрывает детали реализации — тест описывает только бизнес-сценарий.
    """
    book_store_registration.register(test_book_store_user_2)
    assert book_store_registration.is_registration_successfully() is True