from time import sleep
from selene import browser, have, be

from tests.heplers import GeneratedFormData


def test_practice_form(browser_open):
    sleep(3)
    browser.should(have.title_containing('demo'))
    browser.should(have.url_containing('demoqa.com'))
    sleep(3)
    browser.element('#firstName').type('John')
    browser.element('#lastName').type('Doe')
    browser.element('#userEmail').type('JohnDoe@email.com')
    gender = browser.element('#genterWrapper')
    gender.all('.form-check').element_by(have.exact_text('Male')).click()
    browser.element('#userNumber').type('+4917635353535')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__year-select').all('option')\
        .element_by(have.exact_text(str(GeneratedFormData.year))).click()
    browser.element('.react-datepicker__month-select').all('option')\
    .element_by(have.exact_text(GeneratedFormData.month)).click()
    browser.element(f'.react-datepicker__day--0{GeneratedFormData.day}').click()

    browser.element('#subjectsInput').click()

    sleep(5)


