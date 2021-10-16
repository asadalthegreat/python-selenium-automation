Feature: Amazon cart

  Scenario: Verify that the cart is empty
    Given I Open Amazon page
    When I click on the cart icon
    Then Cart is Empty text appears

  Scenario: Add item to cart and verify
    Given I Open Amazon page
    When Input road bike into amazon search
    When I click on amazon search icon
    When I select the road bike I want
    When I click add to cart
    When I click on the cart icon
    Then I verify the item is in the cart