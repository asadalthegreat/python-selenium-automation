# Below The Arithmetical Mean
# When given a list, the program should return a list of all the elements below
# the original list’s arithmetical mean. The arithmetical mean is the sum of all elements
# divided by the number of elements.
# Example: [1, 3, 5, 6, 4, 10, 2, 3] (The arithmetical mean is 4.25),
# Return [1, 3, 4, 2, 3]
#
# def below_mean(list):
#     mean = sum(list) / len(list)
#     x = 0
#     output = []
#     for i in list:
#         if list[x] < mean:
#             output.append(list[x])
#         x = x + 1
#     return output
#
#
# test = [1, 3, 5, 6, 4, 10, 2, 3]
# output = below_mean(test)
# print(output)




# Two Lowest Elements
# When given a list of elements, find the two lowest elements.
# They can be equal to each other or different.
# Example: [198, 3, 4, 9, 10, 9, 2], Return: 2, 3

def two_lowest(list):
    x = 0
    lows = [list[0], list[1]]
    for i in list:
        if list[x] < list[0]:
            lows[0] = list[x]
        elif list[x] < list[1]:
            lows[1] = list[x]
        x = x + 1
    return lows

test = [198, 3, 4, 9, 10, 9, 2]
print(two_lowest(test))