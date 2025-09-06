"""
LeetCode Problem 206: Reverse Linked List

Problem Description:
Given the head of a singly linked list, reverse the list, and return the reversed list.

Time Complexity: O(n) where n is the number of nodes
Space Complexity: O(1) - iterative approach using constant extra space

Example:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Input: head = [1,2]
Output: [2,1]

Input: head = []
Output: []
"""

def reverseList(self, head: ListNode) -> ListNode:
        if head == None:
            return head
        if head.next == None:
            return head
        curr = ListNode(0)
        fast = ListNode(0)
        curr = head.next
        fast = curr.next
        head.next = None
        while fast!=None:
            curr.next = head
            head = curr
            curr = fast
            fast = fast.next
        curr.next = head
        head = curr
        return head