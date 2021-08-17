from heapq import *
def reorganizeString(s):
	frequency = {}

	for i in s:
		frequency[i] = frequency.get(i, 0) + 1

	prevChar = None
	prevFreq = None
	result = []
	maxHeap = []

	for i in frequency:
		heappush(maxHeap, (-frequency[i], i))
	
	while maxHeap:
		currFreq, currChar = heappop(maxHeap)
		currFreq = -currFreq
		result.append(currChar)

		if prevChar is not None and prevFreq > 0:				
			heappush(maxHeap, (-prevFreq, prevChar))

		prevChar = currChar
		prevFreq = currFreq - 1

	if len(result) == len(s):
		return ''.join(result)
	else:
		return ''
print(reorganizeString("aabbaabccddba"))