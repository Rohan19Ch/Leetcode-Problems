"""
LeetCode Problem 8: String to Integer (atoi)

Problem Description:
Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer.
The algorithm for myAtoi(string s) is as follows:
1. Read in and ignore any leading whitespace.
2. Check if the next character (if not already at the end of the string) is '-' or '+'.
3. Read in next the characters until the next non-digit character or the end of the input is reached.
4. Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32).
5. If the integer is out of the 32-bit signed integer range [-2^31, 2^31 - 1], then clamp the integer.

Time Complexity: O(n) where n is the length of the string
Space Complexity: O(1) - only using constant extra space

Example:
Input: s = "42"
Output: 42

Input: s = "   -42"
Output: -42

Input: s = "4193 with words"
Output: 4193

Input: s = "words and 987"
Output: 0
"""

def myAtoi(s):
	text = s.lstrip()
	answer = 0
	sign = False
	i = 0
	if len(text) == 0:
		return 0
	if text[0] == "-":
		sign = True
		i = 1
	if text[0] == "+":
		i = 1
	while i < len(text):
		value = text[i]
		try:
			value = int(value)
			answer = answer*10 + value
			i+=1
		except:
			break
	if sign:
		if abs(answer) > 2**31:
			return -2**31
		return -answer
	else:
		if abs(answer) > 2**31-1:
			return 2**31-1
		return answer

print(myAtoi("+-12"))