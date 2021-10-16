Feature: Amazon Search Cancel Order

  Scenario: User can search help for Cancel Order
    Given I Open Amazon help page
    When I input Cancel Order into the search help library field
    When I hit enter
    Then Cancel Items or Orders text appears
