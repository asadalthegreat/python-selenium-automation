# Calculate sum and multiplication of all elements of a list

# 0(N)
def find_sum_and_mult(arr):
    sum_result = 0
    mult_result = 1
    for num in arr:
        sum_result = sum_result + num
        mult_result = mult_result * num

    return [sum_result, mult_result]

test_list = [1,7,3]
print(find_sum_and_mult(test_list))


# List of random numbers.
# Find and print the max element and the index of this element
#
# 0(N)
def find_max_element(arr):
    max_index = 0
    max_value = arr[max_index]

    for i in range(1, len(arr)):
        if arr[i] > max_value:
            max_index = i
            max_value = arr[i]

    return [max_index, max_value]

test = [1, 45, 33, 76, 9, 10]
print(find_max_element(test))

# Find a sum of elements between min and max
# Min and max are not included
# all numbers are unique

# 0(n)
def sum_between_min_max(arr):
    if len(arr) <= 2:
        return -1

    min_value = max_value = arr[0]
    min_index = max_index = i = 0
    while i < len(arr):
        if arr[i] > max_value:
            max_value = arr[i]
            max_index = i
        if arr[i] < min_value:
            min_value = arr[i]
            min_index = i
        i = i + 1

    return sum(arr[min(min_index, max_index) + 1:max(min_index, max_index)])


test = [19, 5, 3, 7, -3, 4, 10]
test1 = [1, 5, 3, 7, -3, 4, 10]

print(sum_between_min_max(test))
print(sum_between_min_max(test1))

# Delete duplicated from sorted array
# Remaining elmts are shifted left to fill emptied indices
# remaining indices are filled with zeroes
# Return number of valid elements
# Cannot use sets

# 0(n)
def delete_dup(arr):
    write_index = 1

    if len(arr) == 1:
        return write_index

    for i in range(1, len(arr)):
        if arr[write_index -1] != arr[i]:
            arr[write_index] = arr[i]
            write_index = write_index + 1

    for i in range(write_index, len(arr)):
        arr[i] = 0

    print(arr)
    return [write_index]


test_list= [1 ,2, 4, 4, 5, 6, 7, 10, 10, 18, 21, 21, 22]
# expected result = [1 ,2, 4, 5, 6, 7, 10, 18, 21, 22, 0, 0, 0]
print(test_list)
print(delete_dup(test_list))


# Enumerate all primes to N
# if input is 18, you should return 2, 3, 5, 7, 11, 13, 17

def generate_prime_nums_to_n(n):
    primes = []
    for i in range(2, n+1):
        for p in range(2, i + 1):
            if p == i:
                primes.append(i)
                break
            if i % p == 0:
                break

    return primes

print(generate_prime_nums_to_n(-1))




# Best time to buy and sell stock
# Given price of stock on a given day, maximize profit by choosing a single day to sell

def buy_and_sell_stock(prices):
    max_sum = current_sum = 0
    for i in range(len(prices) - 1):
        current_sum = current_sum + prices[i + 1] - prices[i]
        if current_sum > max_sum:
            max_sum = current_sum
        if current_sum < 0:
            current_sum = 0

    return max_sum

#
# test_prices = [7,1,5,3,6,4]
# print(buy_and_sell_stock(test_prices))

# Given an array of prices, buy and sell stocks

def buy_and_sell_stock(prices):
    profit = 0

    for i in range(len(prices) - 1):
        if prices[i + 1] > prices[i]:
            profit = profit + profit[i + 1] - prices[i]

    return profit

prices = [7,1,5,3,6,4]
print(buy_and_sell_stock(prices))
