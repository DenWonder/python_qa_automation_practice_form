from selene import have, command, be
from selene.support.shared import browser


class NavigationPanel:
    def __init__(self):
        self.container = browser.element('.left-pannel')

    def open(self, item):
        self.container.all('.menu-item').element_by(have.exact_text(item)).click()
        return self



