Feature: Tests for product page

  Scenario: User can select dress colors
    Given Open Amazon product B07NF5WGQ1 page
    Then Verify user can click through colors
    
  Scenario: User can select crypto degen shirt colors
    Given Open Amazon product B08WM76NL1 page
    Then Verify user can click through degenerate colors
