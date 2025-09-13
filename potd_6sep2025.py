'''Find length of Loop

Given the head of a linked list, determine whether the list contains a loop. If a loop is present, return the number of nodes in the loop, otherwise return 0.
Note: Internally, pos(1 based index) is used to denote the position of the node that tail's next pointer is connected to. If pos = 0, it means the last node points to null, indicating there is no loop. Note that pos is not passed as a parameter.

Examples:
Input: pos = 2,  
Output: 4
Explanation: There exists a loop in the linked list and the length of the loop is 4.

Input: pos = 3, 
Output: 3
Explanation: The loop is from 19 to 10. So length of loop is 19 → 33 → 10 = 3.

Input: pos = 0,   
Output: 0
Explanation: There is no loop.

Constraints:
1 ≤ number of nodes ≤ 105
1 ≤ node->data ≤ 104
0 ≤ pos < number of nodes

Expected Complexities
Time Complexity: O(n)
Auxiliary Space: O(1)
'''
#  Node structure
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None

# Returns count of nodes present in loop.
def countNodes(node):
    res = 1
    curr = node
    while curr.next != node:
        res += 1
        curr = curr.next
    return res

def lengthOfLoop(head):
    slow = head
    fast = head

    while slow is not None and fast is not None \
          and fast.next is not None:

        slow = slow.next
        fast = fast.next.next

        # if slow and fast meet at
        # some point then there is a loop
        if slow == fast:
            return countNodes(slow)

    return 0

if __name__ == "__main__":
    
    head = Node(25)
    head.next = Node(14)
    head.next.next = Node(19)
    head.next.next.next = Node(33)
    head.next.next.next.next = Node(10)
    
    head.next.next.next.next.next = head.next.next
    
    print(lengthOfLoop(head))