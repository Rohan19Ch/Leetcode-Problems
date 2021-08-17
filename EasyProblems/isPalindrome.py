def isPalindrome(x):
	x = str(x)
	rev = x[::-1]
	print(x)
	print(rev)
	if x == rev:
		return 'true'
	else:
		return 'false'
print(isPalindrome(-121))