"""
LeetCode Problem 215: Kth Largest Element in an Array

Problem Description:
Given an integer array nums and an integer k, return the kth largest element in the array.
Note that it is the kth largest element in the sorted order, not the kth distinct element.

Time Complexity: O(n log k) where n is the length of the array
Space Complexity: O(k) for the min heap

Example:
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4

Approach: Use a min heap of size k to keep track of the k largest elements.
The root of the heap will be the kth largest element.
"""

import heapq as hq
def findkthlargest(nums, k):
	minHeap = []
	for i in range(k):
		hq.heappush(minHeap, nums[i])
	i += 1
	while i < len(nums):
		if nums[i] > minHeap[0]:
			hq.heappop(minHeap)
			hq.heappush(minHeap, nums[i])
		i += 1
	return minHeap
print(findkthlargest([-1, 2, 0], 2))