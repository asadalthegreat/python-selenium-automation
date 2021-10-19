Feature: Test for whole foods

  Scenario: Products have a regular price and product name
    Given I Open Amazon Whole Foods page
    Then I verify that every product has text Regular and product name