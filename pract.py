import math
import os
import random
import re
import sys


def maxSubArray(nums):
    maxSub = nums[0]
    count = 0

    for num in nums:
        if count < 0:
            count = 0
        count += num
        maxSub = max(maxSub, count)
    return maxSub


print(maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))


# def countAndSay(n):
#     if n == 1:
#         return "1"


# countAndSay()


# def strStr(haystack, needle):
#     # find if the substring 'needle' exist in a string 'haystack'
#     # return index of the first letter in the substring
#     # return -1 otherwise

#     # The find() method finds the first occurrence of the specified value.
#     # The find() method returns -1 if the value is not found.
#     # The find() method is almost the same as the index() method, the only difference is that the index() method raises an exception if the value is not found. (See example below)
#     # Plan
#     # if needle string is empty, return zero
#     if len(needle) == 0:
#         return 0
#     # loop through haystack string
#     if needle in haystack:
#         return haystack.find(needle)
#     else:
#         return -1


# print(strStr('hello', 'll'))


# def isValid(s):
#     stack = []
#     dict = {'(': ')', '[': ']', '{': '}'}

#     for char in s:
#         if char in dict:
#             stack.append(dict[char])
#         else:
#             if len(stack) == 0 or stack.pop() != char:
#                 return False

#     return len(stack) == 0


# print(isValid("{()}"))

# def longestCommonPrefix(strs):
#     prefix = strs[0]
#     length = len(prefix)

#     if len(strs) == 0:
#         return("")
#     if len(strs) == 1:
#         return(strs[0])

#     for char in strs[1:]:
#         while prefix != char[0:length]:
#             prefix = prefix[0:length - 1]
#             length -= 1
#             if length == 0:
#                 return("")
#     return prefix


# print(longestCommonPrefix(["flower", "flow", "flight"]))


# def romanToInt(s):
#     dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500,
#             "M": 1000, }
#     converted_num = 0
#     for i in range(len(s)):
#         curr = dict.get(s[i])
#         next_num = dict.get(s[i + 1]) if i+1 < len(s) else 0
#         if curr >= next_num:
#             converted_num += curr
#         else:
#             converted_num -= curr
#     return converted_num


# romanToInt("MCMXCIV")


# def isPalindrome(x):
#     modded = 0
#     if x < 0 or x % 10 == 0 and x != 0:
#         return False
#     if x > 0 and x < 10:
#         return True
#     while x > modded:
#         modded = modded * 10 + (x % 10)
#         x //= 10
#     print(modded)
#     print(x)
#     if x == modded or x == modded//10:
#         return True
#     else:
#         return False


# print(isPalindrome(100))


# def reverse(x):
#     digits = [int(num) for num in str(x)]
#     reversed_digits = []
#     for char in digits:
#         popped = digits.pop()
#         reversed_digits.append(popped)
#     print(digits)
#     print(reversed_digits)
#     # """
#     # :type x: int
#     # :rtype: int
#     # """


# print(reverse(123))


# def repeatedSubstringPattern(s):
#     # """
#     # :type s: str
#     # :rtype: bool
#     #  """

#     substring = ""
#     for i in range(len(s) // 2):
#         substring += s[i]
#         if len(s) % len(substring) == 0:
#             if substring * (len(s) // len(substring)) == s:
#                 return True
#     return False


# print(repeatedSubstringPattern("abab"))


# def minimumBribes(q):
#     counter = 0
#     for i in range(len(q)):


# minimumBribes([2, 1, 5, 3, 4])


# # Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#         # """
#         # :type l1: ListNode
#         # :type l2: ListNode
#         # :rtype: ListNode
#         # """


# def addTwoNumbers(l1, l2):
#     cur_carry = 0

#     head = cur = ListNode(0)
#     cur_1 = l1
#     cur_2 = l2

#     while cur_1 or cur_2:
#         sum_list = cur_carry
#         # sum_list = cur_1.val + cur_2.val
#         sum_list += 0 if cur_1 is None else cur_1.val
#         sum_list += 0 if cur_2 is None else cur_2.val
#         print(sum_list, cur_1.val)

#         if sum_list >= 10:
#             sum_list -= 10
#             cur_carry = 1
#         else:
#             cur_carry = 0

#         cur.next = ListNode(sum_list)
#         cur = cur.next

#         if cur_1 is None and cur_2 is None:
#             break
#         elif cur_1 is None:
#             cur_2 = cur_2.next
#         elif cur_2 is None:
#             cur_1 = cur_1.next
#         else:
#             cur_1 = cur_1.next
#             cur_2 = cur_2.next
#         # if cur.val is None:
#         #     cur.val = sum_list
#         # else:
#         #     cur.next = sum_list
#         # cur_1 = cur_1.next
#         # cur_2 = cur_2.next
#     return head.next


# def linked_str(l):
#     if l is None:
#         return ''
#     return str(l.val) + '->' + linked_str(l.next)


# l1 = ListNode(2)
# l1.next = ListNode(4)
# l1.next.next = ListNode(3)
# # print(linked_str(l1))

# l2 = ListNode(5)
# l2.next = ListNode(6)
# l2.next.next = ListNode(4)
# # print(linked_str(l2))

# print(linked_str(addTwoNumbers(l1, l2)))


# # # Complete the rotLeft function below.
# def rotLeft(a, d):
#     temp = []
#     for i in range(0, d):
#         temp = a[0]

#         for j in range(0, len(a) - 1):
#             a[j] = a[j + 1]
#         a[len(a) - 1] = temp
#     return a

# # print(temp)


# print(rotLeft([1, 2, 3, 4, 5], 2))


# print(rotLeft([1, 2, 3, 4, 5], 2))

# arr = [
#     [1, 1, 1, 0, 0, 0],
#     [0, 1, 0, 0, 0, 0],
#     [1, 1, 1, 0, 0, 0],
#     [0, 0, 2, 4, 4, 0],
#     [0, 0, 0, 2, 0, 0],
#     [0, 0, 1, 2, 4, 0]
# ]
# rows = len(arr)
# cols = len(arr[0])

# max_sum = []
# for i in range(rows - 2):
#     for j in range(cols - 2):
#         hourglass_sum = arr[i][j] + arr[i][j + 1] + arr[i][j + 2] + arr[i +
#                                                                         1][j + 1] + arr[i + 2][j] + arr[i + 2][j + 1] + arr[i + 2][j + 2]
#         max_sum.append(hourglass_sum)


# def hourglassSum(arr):

# def twoSum(nums, target):
#     seen = {}
#     for i, num in enumerate(nums):
#         n = target - num
#         # print(n)
#         if n not in seen:
#             seen[num] = i
#         else:
#             return [seen[n], i]

# print(twoSum([3, 2, 4], 6))

# Complete the repeatedString function below.

# def repeatedString(s, n):
#     total = 0
#     for var in s:
#         if var == 'a':
#             total += 1

#     return total

# print(repeatedString('abcacabcac', 10)

# Complete the jumpingOnClouds function below.

# def jumpingOnClouds(c):
#     path_counter = 0
#     i = 0
#     while i < len(c) - 1:
#         if c[i] == c.length or c[i + 2] == 1:
#             i += 1
#             path_counter += 1
#         else:
#             i += 2
#             path_counter += 1

#     return path_counter

# print(jumpingOnClouds([0, 0, 1, 0, 0, 1, 0]))
# print(jumpingOnClouds([0, 0, 0, 0, 1, 0]))
