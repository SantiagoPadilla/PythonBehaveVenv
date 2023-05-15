@regression
Feature: Validate paragraphs on the home page

    This test case verifies that the feature retrieves the text paragraphs on the home page and compares them to the expected text paragraphs.


    Scenario: Home paragraphs

        Given I navite to the site "bcncgroup.com"
        And I accept "cookies"
        Then the page title should be "BCNC"
        And I click on the page element "Home title"
        And the current site is "bcncgroup.com"
        And I verify the expected "home paragraphs" texts

