/*Linked List Group Reverse

You are given the head of a Singly linked list. You have to reverse every k node in the linked list and return the head of the modified list.
Note: If the number of nodes is not a multiple of k then the left-out nodes at the end, should be considered as a group and must be reversed.

Examples:
Input: k = 2,   
Output: 2 -> 1 -> 4 -> 3 -> 6 -> 5
Explanation: Linked List is reversed in a group of size k = 2.
   
Input: k = 4,   
Output: 4 -> 3 -> 2 -> 1 -> 6 -> 5
Explanation: Linked List is reversed in a group of size k = 4.
   
Constraints:
1 ≤ size of linked list ≤ 105
0 ≤ node->data ≤ 106
1 ≤ k ≤ size of linked list 

Expected Complexities
Time Complexity: O(n)
Auxiliary Space: O(1)*/
class Node {
    int data;
    Node next;

    Node(int x) {
        data = x;
        next = null;
    }
}
public class potd_4sep2025 {
    static Node reverseKGroup(Node head, int k) {
        if (head == null) {
            return head;
        }

        Node curr = head;
        Node newHead = null;
        Node tail = null;

        while (curr != null) {
            Node groupHead = curr;
            Node prev = null;
            Node nextNode = null;
            int count = 0;

            // Reverse the nodes in the current group
            while (curr != null && count < k) {
                nextNode = curr.next;
                curr.next = prev;
                prev = curr;
                curr = nextNode;
                count++;
            }

            // If newHead is null, set it to the
            // last node of the first group
            if (newHead == null) {
                newHead = prev;
            }

            // Connect the previous group to the 
            // current reversed group
            if (tail != null) {
                tail.next = prev;
            }

            // Move tail to the end of the
          	// reversed group
            tail = groupHead;
        }

        return newHead;
    }

 static void printList(Node head) {
        Node curr = head;
        while (curr != null) {
            System.out.print(curr.data);
            if(curr.next != null){
                System.out.print(" -> ");
            }
            curr = curr.next;
        }
        System.out.println();
    }
    public static void main(String[] args) {

        Node head = new Node(1);
        head.next = new Node(2);
        head.next.next = new Node(3);
        head.next.next.next = new Node(4);
        head.next.next.next.next = new Node(5);

        head = reverseKGroup(head, 3);
        printList(head);
    }

}
