from behave import given, when, then
from common_selenium import webSelenium
from common_configs import urlConfig


@given('I navite to the site "{site}"')
def navigate_to_url(context, site):
    url = urlConfig.URLCONFIG.get(site)
    
    context.driver = webSelenium.go_to(url)
    pass

@given('the page title should be "{expected_title}"')
def verify_page_title(context, expected_title):
    webSelenium.assert_page_title(context, expected_title)

@then('the page title should be "{expected_title}"')
def verify_page_title(context, expected_title):
    webSelenium.assert_page_title(context, expected_title)

@then('the current site is "{site}"')
def verify_current_url(context, site):
    url = urlConfig.URLCONFIG.get(site)
    
    webSelenium.assert_current_url(context, url)


