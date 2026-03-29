import os.path
from time import sleep
from selene import browser, have

from tests.endpoints import Endpoints


def test_practice_form(browser_config):
    browser.open(Endpoints.AUTOMATION_PRACTICE_FORM_URL)
    sleep(3)
    browser.should(have.title_containing('demo'))
    browser.should(have.url_containing('demoqa.com'))
    sleep(1)
    browser.element('#firstName').type('John')
    browser.element('#lastName').type('Doe')
    browser.element('#userEmail').type('JohnDoe@email.com')
    gender = browser.element('#genterWrapper')
    gender.all('.form-check').element_by(have.exact_text('Male')).click()
    browser.element('#userNumber').type('1234567890')

    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__year-select').all('option')\
        .element_by(have.exact_text(str(1990))).click()
    browser.element('.react-datepicker__month-select').all('option')\
    .element_by(have.exact_text("March")).click()
    browser.element(f'.react-datepicker__day--0{11}').click()

    browser.element('#subjectsInput').click()
    browser.element('#subjectsInput').type("Maths").press_enter()

    hobbies = browser.element('#hobbiesWrapper')
    hobbies.all('.form-check').element_by(have.exact_text('Music')).click()

    browser.element('#uploadPicture').set_value(
        os.path.join(os.path.dirname(os.path.abspath('.')), "resources", "img.jpg")
    )

    browser.element('#currentAddress').set_value("Munchen, Germany, Biertrinkenstrasse, 14")

    browser.element('#state').click()

    states = browser.element('#react-select-3-listbox')
    states.all('div[role="option"]').element_by(have.exact_text('NCR')).click()


    browser.element('#city').click()
    cities = browser.element('#react-select-4-listbox')
    cities.all('div[role="option"]').element_by(have.exact_text('Noida')).click()

    sleep(1)

    browser.element('#submit').click()

    sleep(1)

    browser.element('.table').all('td').even.should(have.exact_texts(
        'John Doe',
        'JohnDoe@email.com',
        'Male',
        '1234567890',
        '11 March,1990',
        'Maths',
        'Music',
        'img.jpg',
        'Munchen, Germany, Biertrinkenstrasse, 14',
        'NCR Noida'
    ))

