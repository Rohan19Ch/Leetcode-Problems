"""
LeetCode Problem 209: Minimum Size Subarray Sum

Problem Description:
Given an array of positive integers nums and a positive integer target, 
return the minimal length of a contiguous subarray [numsl, numsl+1, ..., numsr-1, numsr] 
of which the sum is greater than or equal to target. If there is no such subarray, return 0 instead.

Time Complexity: O(n) where n is the length of the array
Space Complexity: O(1) - only using constant extra space

Example:
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.

Input: target = 4, nums = [1,4,4]
Output: 1

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0

Approach: Sliding window technique with two pointers.
"""

def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ws = 0
        we = 0
        winSum = 0
        length = len(nums)
        minL = math.inf
        while we < length:
            winSum += nums[we]
            while winSum >= target:
                minL = min(minL, we-ws+1)
                winSum = winSum - nums[ws]
                ws += 1
            we += 1
        if minL == math.inf:
            return 0
        else:
            return minL