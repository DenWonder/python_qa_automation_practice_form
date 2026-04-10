import allure
import pytest
import os
from selene.support.shared import browser
from selenium import webdriver
from demoqa.endpoints import Endpoints
from demoqa.model.pages.automation_practice_form import AutomationPracticeForm
from demoqa.model.pages.text_box_form import TextBoxForm


@pytest.fixture(autouse=True)
def browser_config():
    options = webdriver.ChromeOptions()

    if os.getenv("CI"):
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

    browser.config.driver_options = options
    browser.config.base_url = Endpoints.BASE_URL
    browser.config.timeout = float(10)
    yield
    browser.quit()

@pytest.fixture()
def practice_form_page():
    practice_form = AutomationPracticeForm()
    practice_form.open()
    return practice_form

@pytest.fixture()
def text_box_page():
    text_box_page = TextBoxForm()
    text_box_page.open()
    return text_box_page

@pytest.fixture()
def web_browser():
    browser.config.window_width = 1920
    browser.config.window_height = 1080

@pytest.fixture()
def mobile_browser():
    browser.config.window_width = 400
    browser.config.window_height = 824

@pytest.fixture()
def tablet_browser():
    browser.config.window_width = 820
    browser.config.window_height = 1180