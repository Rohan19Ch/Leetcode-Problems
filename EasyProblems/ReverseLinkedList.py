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