"""
LeetCode Problem 767: Reorganize String

Problem Description:
Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.
Return any possible rearrangement of s or return "" if not possible.

Time Complexity: O(n log k) where n is the length of string and k is the number of unique characters
Space Complexity: O(k) for the heap and frequency map

Example:
Input: s = "aab"
Output: "aba"

Input: s = "aaab"
Output: ""

Approach: Use a max heap to always pick the most frequent character that's different from the previous one.
"""

from heapq import *
def reorganizeString(s):
	frequency = {}

	for i in s:
		frequency[i] = frequency.get(i, 0) + 1

	prevChar = None
	prevFreq = None
	result = []
	maxHeap = []

	for i in frequency:
		heappush(maxHeap, (-frequency[i], i))
	
	while maxHeap:
		currFreq, currChar = heappop(maxHeap)
		currFreq = -currFreq
		result.append(currChar)

		if prevChar is not None and prevFreq > 0:				
			heappush(maxHeap, (-prevFreq, prevChar))

		prevChar = currChar
		prevFreq = currFreq - 1

	if len(result) == len(s):
		return ''.join(result)
	else:
		return ''
print(reorganizeString("aabbaabccddba"))