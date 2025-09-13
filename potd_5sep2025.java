/* Sort a linked list of 0s, 1s and 2s
Given the head of a linked list where nodes can contain values 0s, 1s, and 2s only. Your task is to rearrange the list so that all 0s appear at the beginning, followed by all 1s, and all 2s are placed at the end.

Examples:
Input: head = 1 → 2 → 2 → 1 → 2 → 0 → 2 → 2  
Output: 0 → 1 → 1 → 2 → 2 → 2 → 2 → 2
Explanation: All the 0s are segregated to the left end of the linked list, 2s to the right end of the list, and 1s in between. The final list will be:
   
Input: head = 2 → 2 → 0 → 1  
Output: 0 → 1 → 2 → 2
Explanation: After arranging all the 0s, 1s and 2s in the given format, the output will be:
   
Constraints:
1 ≤ no. of nodes ≤ 106
0 ≤ node->data ≤ 2

Expected Complexities
Time Complexity: O(n)
Auxiliary Space: O(1)
 */
class Node {
    int data;
    Node next;

    Node(int new_data) {
        data = new_data;
        next = null;
    }
}
 
public class potd_5sep2025 {
    static Node segregate(Node head) {
        if (head == null || head.next == null) 
            return head; 

        Node zeroD = new Node(0); 
        Node oneD = new Node(0); 
        Node twoD = new Node(0);

        Node zero = zeroD, one = oneD, two = twoD; 

        // traverse list 
        Node curr = head; 
        while (curr != null) { 
            if (curr.data == 0) { 
              	
                // if the data of current node is 0, 
                // append it to pointer zero and update zero
                zero.next = curr; 
                zero = zero.next; 
            } 
            else if (curr.data == 1) { 
              	
                // if the data of current node is 1, 
                // append it to pointer one and update one
                one.next = curr; 
                one = one.next; 
            } 
            else { 
              	
                // if the data of current node is 2, 
                // append it to pointer two and update two
                two.next = curr; 
                two = two.next; 
            } 
            curr = curr.next; 
        } 

        // combine the three lists
        zero.next = (oneD.next != null) ? (oneD.next) : (twoD.next); 
        one.next = twoD.next; 
        two.next = null; 
          
        // updated head 
        head = zeroD.next; 

        return head; 
    } 

    public static void main(String[] args) {
        
        Node head = new Node(1);
        head.next = new Node(2);
        head.next.next = new Node(2);
        head.next.next.next = new Node(1);
        head.next.next.next.next = new Node(2);
        head.next.next.next.next.next = new Node(0);
        head.next.next.next.next.next.next = new Node(2);
        head.next.next.next.next.next.next.next = new Node(2);
    
       
        head = segregate(head);
        while (head != null) {
            System.out.print(head.data);
            if(head.next != null){
                System.out.print(" -> ");
            }
            head = head.next;
        }
        System.out.println();
    }

}
