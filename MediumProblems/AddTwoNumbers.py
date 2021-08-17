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