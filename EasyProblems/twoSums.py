"""
LeetCode Problem 1: Two Sum

Problem Description:
Given an array of integers nums and an integer target, return indices of the two numbers 
such that they add up to target. You may assume that each input would have exactly one solution, 
and you may not use the same element twice.

Time Complexity: O(n²) - brute force approach with nested loops
Space Complexity: O(1) - no extra space used

Example:
Input: nums = [2,7,11,15], target = 9
Output: [0,1] (Because nums[0] + nums[1] = 2 + 7 = 9)

Input: nums = [3,2,4], target = 6
Output: [1,2]

Input: nums = [3,3], target = 6
Output: [0,1]

Note: This is a brute force solution. A more optimal O(n) solution using hash map exists.
"""

def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        length = len(nums)
        for i in range(length):
            for j in range(length):
                if nums[i]+nums[j] == target and i!=j:
                    return [i, j]