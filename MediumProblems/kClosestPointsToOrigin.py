"""
LeetCode Problem 973: K Closest Points to Origin

Problem Description:
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane 
and an integer k, return the k closest points to the origin (0, 0).
The distance between two points on the X-Y plane is the Euclidean distance 
(i.e., √((x1 - x2)² + (y1 - y2)²)).

Time Complexity: O(n log k) where n is the number of points
Space Complexity: O(k) for the heap

Example:
Input: points = [[1,1],[3,3],[2,-1]], k = 2
Output: [[1,1],[2,-1]]

Input: points = [[3,3],[5,-1],[-2,4]], k = 2
Output: [[3,3],[-2,4]]

Approach: Use a max heap to keep track of the k closest points.
Note: We use negative distances to simulate max heap using Python's min heap.
"""

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