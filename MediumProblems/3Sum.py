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