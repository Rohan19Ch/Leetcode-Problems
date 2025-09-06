"""
LeetCode Problem 347: Top K Frequent Elements

Problem Description:
Given an integer array nums and an integer k, return the k most frequent elements. 
You may return the answer in any order.

Time Complexity: O(n log k) where n is the length of the array
Space Complexity: O(n) for the frequency map

Example:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Input: nums = [1], k = 1
Output: [1]

Note: This implementation only builds the frequency map but doesn't complete the k selection.
A complete solution would use a heap or sorting to find the top k elements.
"""

def topKFrequent(nums, k):
	dic = {}
	for i in nums:
		try:
			dic[i] += 1
		except:
			dic[i] = 1
	print(dic)
topKFrequent([1,1,1,2,2,3], 3)