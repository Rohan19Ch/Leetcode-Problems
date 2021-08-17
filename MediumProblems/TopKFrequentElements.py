def topKFrequent(nums, k):
	dic = {}
	for i in nums:
		try:
			dic[i] += 1
		except:
			dic[i] = 1
	print(dic)
topKFrequent([1,1,1,2,2,3], 3)