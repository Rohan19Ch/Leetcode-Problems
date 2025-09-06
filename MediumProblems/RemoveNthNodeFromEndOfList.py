"""
LeetCode Problem 19: Remove Nth Node From End of List

Problem Description:
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Time Complexity: O(L) where L is the length of the linked list
Space Complexity: O(1) - only using constant extra space

Example:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Input: head = [1], n = 1
Output: []

Input: head = [1,2], n = 1
Output: [1]

Approach: Two-pointer technique - maintain n distance between two pointers.
"""

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