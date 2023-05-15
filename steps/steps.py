from behave import given, when, then
import logging as log
from common_steps import commonSteps
from common_selenium import webSelenium
from common_configs import locatorConfig
from common_data import bcncgroupData
import time

@then('The "{navBar}" bar should be visible')
def verify_nav_bars_visible(context, navBar):
    expectedBars = ['Home','Who we are','Services','Expertise','Contact']
    if navBar not in expectedBars:
        raise Exception("The passed in navBar type is not one of expected.")
    
    locatorElement = locatorConfig.HOME_LOCATORS.get(navBar)

    navElement = webSelenium.findElement(context, locatorElement['type'], locatorElement['locator'])
    
    webSelenium.assertVisible(navElement)
    pass

@then('I verify the expected "{paragraphs}" texts')
def verify_current_texts(context, paragraphs):
    expectedTexts = bcncgroupData.PARAGRAPHS.get(paragraphs)
    locatorElement = locatorConfig.HOME_LOCATORS.get(paragraphs)
    
    webSelenium.assert_array_of_texts(context, locatorElement['type'], locatorElement['locator'], expectedTexts)

@when('I click on "{clicked_button}" button')
def click_on_url_button(context, clicked_button):
    time.sleep(10)
    locatorElement = locatorConfig.HOME_LOCATORS.get(clicked_button)
    webSelenium.clickOnElement(context, locatorElement['type'], locatorElement['locator'])
    pass

@given('I accept "{cookies}"')
def accept_cookies(context, cookies):
    time.sleep(10)
    locatorElement = locatorConfig.HOME_LOCATORS.get(cookies)
    
    webSelenium.clickOnElement(context, locatorElement['type'], locatorElement['locator'])
    time.sleep(10)
    pass

@then('I click on the page element "{title}"')
def click_on_element(context, title):

    locatorElement = locatorConfig.HOME_LOCATORS.get(title)
    
    webSelenium.clickOnElement(context, locatorElement['type'], locatorElement['locator'])
    pass