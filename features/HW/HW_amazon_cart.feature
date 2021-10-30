Feature: Amazon cart

  Scenario: Verify that the cart is empty
    Given I Open Amazon page
    When I click on the cart icon
    Then Cart is Empty text appears

#  There is some flakiness in this test due to an amazon bug:
#  Click on add to cart from the item page only works properly sometimes
  Scenario: Add item to cart and verify
    Given I Open Amazon page
    When Input ilm bike helmet men into amazon search
    When I click on amazon search icon
    When I select the helmet I want
    When I click add to cart
    When I click on the cart icon
    Then I verify the item is in the cart
