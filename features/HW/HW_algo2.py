# Split in Half
# Given a string. Split it into two equal parts. Swap these parts and return the result.
# If the string has odd characters, the first part should be one character greater than the second part.
# Example: string = 'bbbbbcaaaaa'. Result = ‘aaaaabbbbbc’.
#

string = input("input a string")
print(string)

if len(string)%2:
    position = int(len(string)/2) + 1

else:
    position = int(len(string)/2)

new = list(string)
new[position] = ('!!!!!' + new[position])
string = ''.join(new)
string2 = string.split("!!!!!")
print(string2[1] + string2[0])



# Unique Characters in String
# Given a string, determine if it consists of all unique characters.
# For example, the string 'abcde' has all unique characters and should return True.
# The string 'aabcde' contains duplicate characters and should return False.
# Hint: https://www.w3schools.com/python/python_sets.asp

a = input("Input a string:")
print(bool(len(set(a)) == len(list(a))))