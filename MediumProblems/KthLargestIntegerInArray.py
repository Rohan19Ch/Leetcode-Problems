"""
LeetCode Problem 1985: Find the Kth Largest Integer in the Array

Problem Description:
You are given an array of strings nums and an integer k. Each string in nums represents an integer without leading zeros.
Return the string that represents the kth largest integer in nums.

Time Complexity: O(n log k) where n is the length of the array
Space Complexity: O(k) for the min heap

Example:
Input: nums = ["3","6","7","10"], k = 4
Output: "3"

Input: nums = ["2","21","12","1"], k = 3
Output: "2"

Input: nums = ["0","0"], k = 2
Output: "0"

Approach: Convert strings to integers, use min heap to find kth largest, then convert back to string.
"""

import heapq as hq
def findkthlargest(nums, k):
	minHeap = []
	for i in range(k):
		hq.heappush(minHeap, int(nums[i]))
	i += 1
	while i < len(nums):
		if int(nums[i]) > minHeap[0]:
			hq.heappop(minHeap)
			hq.heappush(minHeap, int(nums[i]))
		i += 1
	return str(minHeap[0])
print(findkthlargest(["3","6","7","10"], 4))