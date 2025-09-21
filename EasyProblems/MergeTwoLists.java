package EasyProblems;


import java.util.List;

class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 }

public class MergeTwoLists {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {

        if(list1 == null && list2 == null) {
            return list1;
        }

        if(list1 == null) {
            return list2;
        }

        if(list2 == null) {
            return list1;
        }

        ListNode mergedList = new ListNode();
        ListNode tail = new ListNode();

        while(list1 != null || list2 != null) {
            if(list1.val <= list2.val) {
                tail.next = list1;
                tail = list1;
                list1 = list1.next;
            }
            else {
                tail.next = list2;
                tail = list2;
                list2 = list2.next;
            }
        }

        if(list1 == null) {
            tail.next = list2;
        }

        if(list2 == null) {
            tail.next = list1;
        }

        return mergedList;


    }
}
