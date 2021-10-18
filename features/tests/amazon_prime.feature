Feature: Amazon Prime tests

  Scenario: Verify user sees correct amount of benefit boxes
    Given I Open Amazon Prime page
    Then Verify 7 benefit modules are present