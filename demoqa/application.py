from selene.support.shared import browser

from demoqa.model.components.navigation_panel import NavigationPanel
from demoqa.model.pages.automation_practice_form import AutomationPracticeForm
from demoqa.model.pages.text_box_form import TextBoxForm


class Application:
    """
        Application Manager - это класс, который инкапсулирует в себе
        все Page Object и другие объекты, необходимые для взаимодействия
        с приложением.

    """
    def __init__(self):
        self.practice_form = AutomationPracticeForm()
        self.text_box_form = TextBoxForm()
        self.navigation_panel = NavigationPanel()

        def open(self):
            browser.open('/')
            return self


app: Application = Application()