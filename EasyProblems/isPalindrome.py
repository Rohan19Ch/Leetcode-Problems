"""
LeetCode Problem 9: Palindrome Number

Problem Description:
Given an integer x, return true if x is palindrome integer.
An integer is a palindrome when it reads the same backward as forward.

Time Complexity: O(log n) where n is the input number
Space Complexity: O(log n) for string conversion

Example:
Input: x = 121
Output: true

Input: x = -121
Output: false (negative numbers are not palindromes)

Input: x = 10
Output: false
"""

def isPalindrome(x):
	x = str(x)
	rev = x[::-1]
	print(x)
	print(rev)
	if x == rev:
		return 'true'
	else:
		return 'false'
print(isPalindrome(-121))