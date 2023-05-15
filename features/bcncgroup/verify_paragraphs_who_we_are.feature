@regression
Feature: Feature name

    This test case verifies that the feature retrieves the text paragraphs on the who we are page and compares them to the expected text paragraphs.


    Scenario: Home paragraphs

        Given I navite to the site "bcncgroup.com"
        And I accept "cookies"
        When I click on "Who we are" button
        Then the page title should be "BCNC"
        And the current site is "bcncgroup.com/who-we-are/"
        And I click on the page element "Who we are title"
        And I verify the expected "How we are paragraphs" texts

