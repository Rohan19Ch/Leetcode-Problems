"""
LeetCode Problem 7: Reverse Integer

Problem Description:
Given a signed 32-bit integer x, return x with its digits reversed. 
If reversing x causes the value to go outside the signed 32-bit integer range [-2^31, 2^31 - 1], 
then return 0.

Time Complexity: O(log n) where n is the input number
Space Complexity: O(log n) for string conversion

Example:
Input: x = 123
Output: 321

Input: x = -123
Output: -321

Input: x = 120
Output: 21
"""

def reverse(x):
	converted = str(abs(x))
	converted = converted[::-1]
	result = int(converted)
	if result > (2**31) - 1:
		return 0
	if x > 0:
		return result
	else:
		return -result
print(reverse(65468138436468454))