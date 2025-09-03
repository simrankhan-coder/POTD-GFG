/*Swap Kth nodes from ends

Given the head of a singly linked list and an integer k. Swap the kth node (1-based index) from the beginning and the kth node from the end of the linked list. Return the head of the final formed list and if it's not possible to swap the nodes return the original list.

Examples:

Input: k = 1,  
Output: 5 -> 2 -> 3 -> 4 -> 1
Explanation: Here k = 1, hence after swapping the 1st node from the beginning and end the new list will be 5 -> 2 -> 3 -> 4 -> 1.
  
Input: k = 2,  
Output: 5 -> 9 -> 8 -> 5 -> 10 -> 3
Explanation: Here k = 2, hence after swapping the 2nd node from the beginning and end the new list will be 5 -> 9 -> 8 -> 5 -> 10 -> 3.
  
Constraints:
1 ≤ list size ≤ 104
1 ≤ node->data ≤ 106
1 ≤ k ≤ 104

Time Complexity: O(n)
Auxiliary Space: O(1)*/
#include <iostream>
using namespace std;

class Node {
public:
    int data;
    Node* next;
    Node(int d) {
        data = d;
        next = nullptr;
    }
};
Node* swapKth(Node* head, int k) {
        // code here
        if (head == NULL) {
            return NULL;
        }

        // Find the k-th node from the beginning
        Node* first_kth = head;
        int count = 1;
        while (count < k) {
            if (first_kth == NULL) {
                // k is out of bounds, no need to swap.
                return head;
            }
            first_kth = first_kth->next;
            count++;
        }
        
        // If first_kth is NULL, it means k is out of bounds.
        if (first_kth == NULL) {
            return head;
        }

        // Find the k-th node from the end using two pointers
        Node* slow = head;
        Node* fast = first_kth;
        
        while (fast->next != NULL) {
            slow = slow->next;
            fast = fast->next;
        }
        
        // At this point, slow is the k-th node from the end
        // and first_kth is the k-th node from the beginning.
        // Swap their data.
        swap(first_kth->data, slow->data);
        
        return head;
    }

// utility to print list
void printList(Node* head) {
    while (head) {
        cout << head->data;
        if (head->next) cout << " -> ";
        head = head->next;
    }
    cout << endl;
}
//Driver Code
int main() {
    
    Node* head = new Node(5);
    head->next = new Node(10);
    head->next->next = new Node(8);
    head->next->next->next = new Node(5);
    head->next->next->next->next = new Node(9);
    head->next->next->next->next->next = new Node(3);

    int k = 2;
    head = swapKth(head, k);

    printList(head);

    return 0;
}