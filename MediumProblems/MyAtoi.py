def myAtoi(s):
	text = s.lstrip()
	answer = 0
	sign = False
	i = 0
	if len(text) == 0:
		return 0
	if text[0] == "-":
		sign = True
		i = 1
	if text[0] == "+":
		i = 1
	while i < len(text):
		value = text[i]
		try:
			value = int(value)
			answer = answer*10 + value
			i+=1
		except:
			break
	if sign:
		if abs(answer) > 2**31:
			return -2**31
		return -answer
	else:
		if abs(answer) > 2**31-1:
			return 2**31-1
		return answer

print(myAtoi("+-12"))