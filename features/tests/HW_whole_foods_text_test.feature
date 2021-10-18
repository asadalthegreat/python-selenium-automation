Feature: Test for whole foods

  Scenario: Products have a regular price and product name
    Given I Open Amazon Whole Foods page
    Then I verify 31 items have 'Regular' text
    Then I verify 31 items have a product name