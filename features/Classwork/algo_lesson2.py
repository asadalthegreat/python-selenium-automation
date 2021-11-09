################# ANAGRAM

# def is_anagram(s1, s2):
#     if len(s1) != len(s2):
#         return False
#
#     return sorted(s1) == sorted(s2)
#
#     count = {}
#
#     for letter in s2:
#         if letter in count:
#             count[letter] += 1
#         else:
#             count[letter] = 1
#
#     for letter in s2:
#         if letter in count:
#             count[letter] -= 1
#         else:
#             count[letter] = 1
#
#     for index in count:
#         if count[index] != 0:
#             return False
#
#     return True
#
# print(is_anagram("aabbccdd", "ddccbbaa")) #True
# print(is_anagram("aabbccdd", "baaaddcc")) #False

############################# PALIDROME
# # 0(1)
#
#
# def is_palindrome(s):
#     return s == s[::-1]
#
# str_pos = "radar"
# str_pos = "radar"
#
# print(is_palindrome(str_pos)) # True
# print(is_palindrome(str_neg)) # False
#
# ######################## ALMOST PALINDROME
#
# def is_almost_palin(s):
#     for i in range(len(s)):
#         t = s[:i] + s[i + 1:]
#         if t == t[::-1]:
#             return True
#
#     return s==s[::-1] # return False
#
# str_pos = "radkar"
# str_neg = "redarop"
#
# print(is_palindrome(str_pos)) # True
# print(is_palindrome(str_neg)) # False
#
# ##################REVERSE STRING




############## COMPRESS

# def compress(s):
#     result = ""
#     length = len(s)
#
#     # edge cases
#     if length == 0:
#         return ""
#     if length == 1:
#         return s + "1"
#
#     last = s[0]
#     cnt = 1
#     i = 1
#
#     while i < length:
#         if s[i] == s[i -1]:
#             cnt += 1
#         else:
#             result = result + s[i - 1] + str(cnt)
#             cnt = 1
#
#         i += 1
#
#     result = result + s[i - 1] + str(cnt)
#
#     return result
#
# print(compress("AAAAaaBBBBCCCCDDEEEEFFF"))


########### REVERSE DIGITS
# 0(1)

# def revers_int(n):
#     s = str(n)
#
#     if s[0] =='-'
#         return int('-' + s[:0:-1])
#     return int(s[::-1])
#
#
# print(reverse_int(123))
# print(reverse_int(-456))