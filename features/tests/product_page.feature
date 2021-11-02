Feature: Tests for product page

  Scenario: User can select dress colors
    Given Open Amazon product B07NF5WGQ1 page
    Then Verify user can click through colors
    
  Scenario: User can select crypto degen shirt colors
    Given Open Amazon product B08WM76NL1 page
    Then Verify user can click through degenerate colors

#    @Lana - the abilty to hover over "New Arrivals" section doesn't appear.
#    I hover over sign in because this is the only component on the page that works
  Scenario: User can hover mouse
    Given Open Amazon product B074TBCSC8 page
    When hover mouse over sign in
    Then Verify sign in component appears
