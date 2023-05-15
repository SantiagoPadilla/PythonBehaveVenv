from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import logging as log
import pytest

def go_to(url):
    driver = webdriver.Chrome()
    url = url.strip()
    driver.get(url)
    driver.maximize_window()
    return driver

def findElement(context, locatorAttr, locatorText):
    try:
        element = context.driver.find_element(locatorAttr, locatorText)
        return element
    except Exception as e:
        raise Exception(e)

def findElements(context, locatorAttr, locatorText):
    try:
        element = context.driver.find_elements(locatorAttr, locatorText)
        return element
    except Exception as e:
        raise Exception(e)

def assertVisible(element):
    if not element.is_displayed():
        raise AssertionError("La condición no se cumple")

def assert_page_title(context, expected_title):
    currentTitle = context.driver.title
    time.sleep(10)
    assert expected_title == currentTitle

def assert_current_url(context, expected_url):
    currentUrl = context.driver.current_url
    assert expected_url == currentUrl
    
def assert_array_of_texts(context, locatorAttr, locatorText, expectedTexts):
    paragraphsElement = findElements(context, locatorAttr, locatorText)
    
    html = context.driver.find_element(By.TAG_NAME, 'html')
    html.send_keys(Keys.END)
    time.sleep(5)
    
    paragraph_texts = []
    for p in paragraphsElement:
        paragraph_text = p.text.strip()
        paragraph_texts.append(paragraph_text)

    log.info("***********expectedTexts*************")
    log.info("*************************************")
    log.info(expectedTexts)
    log.info("***********paragraph_texts*************")
    log.info("*************************************")
    log.info(paragraph_texts)
    
    
    assert expectedTexts == paragraph_texts
    
    pass

def clickOnElement(context, locatorAttr, locatorText):

    try:
        waitElementIsVisible(context, locatorAttr, locatorText)
        element = WebDriverWait(context.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, locatorText))
        )
        element.click()
        
    except Exception as e:
        raise Exception(e)

def waitElementIsVisible(context, locatorAttr, locatorText):
    try:
        WebDriverWait(context.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, locatorText))
        )
    except Exception as e:
        raise Exception(e)