def reverse(x):
	converted = str(abs(x))
	converted = converted[::-1]
	result = int(converted)
	if result > (2**31) - 1:
		return 0
	if x > 0:
		return result
	else:
		return -result
print(reverse(65468138436468454))