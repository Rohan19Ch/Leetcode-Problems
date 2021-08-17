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