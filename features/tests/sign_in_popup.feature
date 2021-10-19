Feature: Amazon Sign in tests

  Scenario: Sign in page can be opened from Sign In popup
    Given I Open Amazon page
    When Click Sign In from popup
    Then Verify Sign In page opens

  Scenario: Sign In popup is visible upon page opening, then disappears
    Given I Open Amazon page
    When Sign In popup appears
    And I wait for 5 seconds
    Then I Verify Sign In popup disappears