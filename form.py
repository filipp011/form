from lib2to3.pgen2 import driver
from selene.support.shared import browser
from selenium.webdriver.common.by import By
import os



def test_form():
    browser.open('https://demoqa.com/automation-practice-form')
    #username
    browser.element('.practice-form-wrapper [id=firstName]').set_value('Filipp')
    #lastname
    browser.element('.practice-form-wrapper [id=lastName]').set_value('Nis')
    #useremail
    browser.element('.practice-form-wrapper [id=userEmail]').set_value('fil.nis61@gmail.com')
    #genderchoose
    browser.element('.custom-radio [id="gender-radio-1"]').double_click()
    #userphone
    browser.element('.practice-form-wrapper [id=userNumber]').set_value('7928179401')
    #b-data
    browser.element('.react-datepicker__input-container [id="dateOfBirthInput"]').click()
    browser.element('.react-datepicker__month-select [value="1"]').click()
    browser.element('.react-datepicker__week [aria-label="Choose Sunday, February 18th, 2024"]').click()
    #subject
    browser.element('.subjects-auto-complete__input [id="subjectsInput"]').type('Hello')
    #hobby
    browser.element('label[for="hobbies-checkbox-1"]').click()
    #uploadphotos
    #browser.element('.form-file [id=uploadPicture]').double_click().type('/Users/filippnis/Downloads-image.jpg')
    #currentAdress
    browser.element('.form-control[id=currentAddress]').type('Москва.ул М.Горькоого 214')
    #state
    browser.element('#state').click()
    browser.element('//div[@id="state"]//div[text()="Haryana"]').click()
    browser.element('#city').click()
    browser.element('//div[@id="city"]//div[text()="Karnal"]').click()
    browser.element('.btn-primary').press_enter()












