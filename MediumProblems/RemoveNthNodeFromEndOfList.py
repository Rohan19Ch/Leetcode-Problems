def removeNthFromEnd(head, n):

	temp = head
	i = 1

	while i < n:
		temp = temp.next
		i += 1

	curr = head
	prev = head
	while temp.next != None:
		prev = curr
		curr = curr.next
		temp = temp.next

	prev.next = curr.next
	curr.next = None

	return head