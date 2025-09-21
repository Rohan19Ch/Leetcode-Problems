package MediumProblems;

class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 }

public class RemoveNthFromEnd {

    public ListNode removeNthFromEnd(ListNode head, int n) {

        ListNode dummy = new ListNode(0);

        dummy.next = head;

        ListNode lastPointer = dummy;
        ListNode nthPointer = dummy;

        int iterator = 0;

        while(iterator <= n) {

            lastPointer = lastPointer.next;

            iterator++;
        }

        while(lastPointer != null) {

            nthPointer = nthPointer.next;
            lastPointer = lastPointer.next;

        }
        if(nthPointer.next == null ){
            return head;
        }

        nthPointer.next = nthPointer.next.next;

        return dummy.next;

    }
}
