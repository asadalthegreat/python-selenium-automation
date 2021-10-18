Feature: Amazon help page tests

  Scenario: User can search help for Cancel Order
    Given I Open Amazon help page
    When I input Cancel Order into the search help library field
    When I hit enter
    Then Cancel Items or Orders text appears

  Scenario: Verify elements on help page are present
    Given I Open Amazon help page
    Then Elements are visible on help page