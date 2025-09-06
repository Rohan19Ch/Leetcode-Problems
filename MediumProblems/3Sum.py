"""
LeetCode Problem 15: 3Sum

Problem Description:
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.

Time Complexity: O(n²) where n is the length of the array
Space Complexity: O(1) ignoring the output array

Example:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

Input: nums = [0,1,1]
Output: []

Input: nums = [0,0,0]
Output: [[0,0,0]]

Approach: Sort the array, then use two pointers technique for each element.
"""

def threeSum(nums):
	nums.sort()

	length = len(nums)
	answer = []

	for i, a in enumerate(nums):
		if i > 0 and a == nums[i-1]:
			continue
		left, right = i+1, length - 1
		while left < right:
			Sum = a + nums[left] + nums[right]
			if Sum > 0:
				right -= 1
			elif Sum < 0:
				left += 1
			else:
				answer.append([a, nums[left], nums[right]])
				left += 1
				while nums[left] == nums[left-1] and left < right:
					left += 1
	return answer
nums = [-1,0,1,0]
print(threeSum(nums))