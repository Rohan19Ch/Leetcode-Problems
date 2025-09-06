"""
LeetCode Problem 14: Longest Common Prefix

Problem Description:
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Time Complexity: O(S) where S is the sum of all characters in all strings
Space Complexity: O(1) ignoring the output space

Example:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Input: strs = ["dog","racecar","car"]
Output: ""
"""

def checkCommon(str1, str2):
	i = 0
	temp = ""
	len1 = len(str1)
	len2 = len(str2)

	while (i < len1) and (i < len2) and (str1[i] == str2[i]):
		temp += str1[i]
		i += 1

	return temp
def longestCommonPrefix(strs):

	if len(strs) == 0:
		return ""

	if len(strs) == 1:
		return strs[0]

	str1 = strs[0]
	str2 = strs[1]
	curr = ""
	curr = checkCommon(str1, str2)

	for string in range(2, len(strs)):
		curr = checkCommon(curr, strs[string])

	return curr
print(longestCommonPrefix(["flower","flow","flight"]))