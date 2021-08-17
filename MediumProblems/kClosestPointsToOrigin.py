from heapq import *
def kClosest(points, k):
	maxHeap = []
	for point in points:
		dist = point[0]**2 + point[1]**2
		heappush(maxHeap, (-dist, point[0], point[1]))
		if len(maxHeap) > k:
			heappop(maxHeap)
	answer = []
	for i in maxHeap:
		answer.append([i[1], i[2]])
	return answer
points = [[3,3],[5,-1],[-2,4]]
k = 2
print(kClosest(points, k))