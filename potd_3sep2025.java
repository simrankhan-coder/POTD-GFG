/*Reverse a Doubly Linked List

You are given the head of a doubly linked list. You have to reverse the doubly linked list and return its head.

Examples:

Input:   
Output: 5 <-> 4 <-> 3
Explanation: After reversing the given doubly linked list the new list will be 5 <-> 4 <-> 3.
   
Input:    
Output: 196 <-> 59 <-> 122 <-> 75
Explanation: After reversing the given doubly linked list the new list will be 196 <-> 59 <-> 122 <-> 75.
   
Constraints:
1 ≤ number of nodes ≤ 106
0 ≤ node->data ≤ 104

Expected Complexities
Time Complexity: O(n)
Auxiliary Space: O(1*/
class Node {
    int data;
    Node next;
    Node prev;

    Node(int data) {
        this.data = data;
        this.next = null;
        this.prev = null;
    }
}
public class potd_3sep2025 {
     static Node reverse(Node head) {
        if (head == null || head.next == null) {
            return head;
        }

        Node currNode = head;
        Node prevNode = null;

        // Traverse the list and reverse the links
        while (currNode != null) {
          
            // Swap the next and prev pointers
            prevNode = currNode.prev;
            currNode.prev = currNode.next;
            currNode.next = prevNode;

            // Move to the next node in the original list
            // (which is now previous due to reversal)
            currNode = currNode.prev;
        }

        head = prevNode.prev;

        return head;
    }

    static void printList(Node node) {
        while (node != null) {
            System.out.print(node.data);
            if(node.next != null){
                System.out.print(" <-> ");
            }
            node = node.next;
        }
        System.out.println();
    }
//Driver Code 
    public static void main(String[] args) {

        Node head = new Node(1);
        head.next = new Node(2);
        head.next.prev = head;
        head.next.next = new Node(3);
        head.next.next.prev = head.next;
        
        head = reverse(head);
        printList(head);
    }
}
