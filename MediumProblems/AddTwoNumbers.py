"""
LeetCode Problem 2: Add Two Numbers

Problem Description:
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.

Time Complexity: O(max(m,n)) where m and n are the lengths of the two linked lists
Space Complexity: O(max(m,n)) for the result linked list

Example:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807

Input: l1 = [0], l2 = [0]
Output: [0]

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
"""

import math
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
def insert(root, item):
    temp = Node(item)
     
    if (root == None):
        root = temp
    else :
        ptr = root
        while (ptr.next != None):
            ptr = ptr.next
        ptr.next = temp
     
    return root
 
def display(root):
    while (root != None) :
        print(root.data, end = " ")
        root = root.next
         
def arrayToList(arr, n):
    root = None
    for i in range(0, n, 1):
        root = insert(root, arr[i])
     
    return root
def AddTwoNumbers(List1, List2):
    ptr1 = List1
    ptr2 = List2
    ptr3 = None
    carry = 0
    while ptr1 != None and ptr2 != None:
        value = (carry+ptr1.data+ptr2.data)%10
        carry = (carry+ptr1.data+ptr2.data)//10
        ptr3 = insert(ptr3, value)
        ptr1 = ptr1.next
        ptr2 = ptr2.next
    while ptr1 != None:
        value = (ptr1.data + carry)%10
        carry = (ptr1.data + carry)//10
        ptr3 = insert(ptr3, value)
        ptr1 = ptr1.next
    while ptr2 != None:
        value = (ptr2.data + carry)%10
        carry = (ptr2.data + carry)//10
        ptr3 = insert(ptr3, value)
        ptr2 = ptr2.next
    if carry == 1:
        ptr3 = insert(ptr3, carry)
    return ptr3
List1 = arrayToList([2,4,3], 3)
List2 = arrayToList([5,6,4], 3)
result = AddTwoNumbers(List1, List2)
display(result)