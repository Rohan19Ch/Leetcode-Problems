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