Feature: Amazon Search

  Scenario: User can search for coffee on Amazon
    Given I Open Amazon page
    When Input coffee into amazon search
    When I click on amazon search icon
    Then I verify "coffee" text is shown

  Scenario: User can search for a table on Amazon
    Given I Open Amazon page
    When Input table into amazon search
    When I click on amazon search icon
    Then I verify "table" text is shown

  Scenario Outline: User can search keywords on Amazon
    Given I Open Amazon page
    When Input <search_word> into amazon search
    When I click on amazon search icon
    Then I verify <result> text is shown
    Examples:
    |search_word   |result     |
    |table         |"table"    |
    |mug           |"mug"      |

