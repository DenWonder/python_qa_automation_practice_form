import pytest
from selene.support.shared import browser

from tests.endpoints import Endpoints


@pytest.fixture()
def browser_config():
    browser.config.base_url = Endpoints.BASE_URL
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.config.headless = False
    browser.config.timeout = float(5)

    yield
    browser.quit()
