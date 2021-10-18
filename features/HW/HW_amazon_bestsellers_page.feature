# Created by jordan at 10/18/21
Feature: Amazon Bestsellers tests

  Scenario: Bestsellers page has expected number of links
    Given I Open Amazon Bestsellers page
    Then Verify 5 navigation links are present