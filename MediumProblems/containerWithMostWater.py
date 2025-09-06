"""
LeetCode Problem 11: Container With Most Water

Problem Description:
You are given an integer array height of length n. There are n vertical lines drawn 
such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container that contains the most water.

Time Complexity: O(n) where n is the length of the array
Space Complexity: O(1) - only using constant extra space

Example:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. 
In this case, the max area of water (blue section) the container can contain is 49.

Input: height = [1,1]
Output: 1

Approach: Two pointers technique - start from both ends and move the pointer with smaller height.
"""

def maxArea(heights):
	left = 0
	right = len(heights) - 1
	result = 0
	while left < right:
		if heights[left] < heights[right]:
			result = max(result, heights[left] * (right - left))
			left += 1
		else:
			result = max(result, heights[right] * (right - left))
			right -= 1
	return result
print(maxArea([1,8,6,2,5,4,8,3,7]))