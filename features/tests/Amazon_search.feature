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

Scenario: User can see language options
  Given I Open Amazon page
  When Hover over language options
  Then Verify correct options present

  Scenario: User can select and search in a department
    Given I Open Amazon page
    When Select department by alias stripbooks
    When Input Faust into amazon search
    And I click on amazon search icon
    Then Verify stripbooks department is selected

  Scenario: User can select and search a department
    Given I Open Amazon page
    When Select department by alias computers
    When Input macbook into amazon search
    And I click on amazon search icon
    Then Verify computers department is selected