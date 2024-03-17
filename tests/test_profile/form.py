from selene.support.shared import browser
from selene import have
import os
import tests


def test_success_profile():
    # Arrange
    browser.driver.maximize_window()
    browser.open('https://demoqa.com/automation-practice-form')

    # Act
    browser.element('#firstName').type('Filipp')
    browser.element('#lastName').type('Nis')
    browser.element('#userEmail').type('fil.nis61@gmail.com')

    browser.element('.custom-radio [id=gender-radio-1]').double_click()
    browser.element('#userNumber').type('7928179401')

    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select [value="1"]').click()
    browser.element('.react-datepicker__week [aria-label="Choose Sunday, February 18th, 2024"]').click()

    browser.element('#subjectsInput').type('English').press_enter()
    browser.element('label[for=hobbies-checkbox-1]').click()

    browser.element('#uploadPicture').set_value(
        os.path.abspath(
            os.path.join(os.path.dirname(tests.__file__), 'resources/foto.jpeg')
        )
    )

    browser.element('#currentAddress').type('Москва.ул М.Горького 214')

    browser.element('#state').click()
    browser.all('[id^=react-select][id*=option]').element_by(
        have.exact_text('NCR')
    ).click()
    browser.element('#city').click()
    browser.all('[id^=react-select][id*=option]').element_by(
        have.exact_text('Delhi')
    ).click()

    browser.element('.btn-primary').press_enter()

    #Assert



















