Feature: Terms and conditions tests

 Scenario: User can open and close Amazon Privacy Notice
    Given I Open Amazon T&C page
    And Store original window
    When I Click on Amazon Privacy Notice link
    And Switch to new window
    Then I Verify Amazon Privacy Notice page is opened
    And User can close new window and switch back to original