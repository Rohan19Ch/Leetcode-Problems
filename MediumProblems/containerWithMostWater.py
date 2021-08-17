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