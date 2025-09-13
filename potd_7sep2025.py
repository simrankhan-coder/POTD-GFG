"""Merge K sorted linked lists
Given an array arr[] of n sorted linked lists of different sizes. Your task is to merge all these lists into a single sorted linked list and return the head of the merged list.

Examples:

Input:  
Output: 1 -> 2 -> 3 -> 4 -> 7 -> 8 -> 9
Explanation: The arr[] has 3 sorted linked list of size 3, 3, 1.
1st list: 1 -> 3 -> 7
2nd list: 2 -> 4 -> 8
3rd list: 9
The merged list will be: 
    
Input   
Output: 1 -> 3 -> 4 -> 5 -> 6 -> 8
Explanation: The arr[] has 3 sorted linked list of size 2, 1, 3.
1st list: 1 -> 3
2nd list: 8
3rd list: 4 -> 5 -> 6
The merged list will be: 
    
Constraints
1 ≤ total no. of nodes ≤ 105
1 ≤ node->data ≤ 103

Expected Complexities
Time Complexity: O(n log n)
Auxiliary Space: O(n)

"""
import heapq

class Node:
    def __init__(self, x):
        self.data = x
        self.next = None

# Function to merge K sorted linked lists
def mergeKLists(arr):
    pq = []
    
    # Insert the head nodes of k lists 
    for i in range(0, len(arr)):
        head = arr[i]
        if head is not None:
            heapq.heappush(pq, (head.data, i, head))
    
    # Initialize a dummy head
    dummy = Node(-1)
    tail = dummy

    while pq:
        
        # Pop the min node
        _, index, top = heapq.heappop(pq)
        
        # Append the node into list
        tail.next = top
        tail = top
        
        # If top node has next node,
        # add it to the heap.
        if top.next is not None:
            heapq.heappush(pq, (top.next.data, index, top.next))

    return dummy.next

def printList(node):
    while node is not None:
        print(node.data, end="")
        if node.next is not None:
            print("->", end="")
        node = node.next
    print()

if __name__ == "__main__":
    k = 3

    arr = [None] * k

    arr[0] = Node(1)
    arr[0].next = Node(3)
    arr[0].next.next = Node(5)
    arr[0].next.next.next = Node(7)

    arr[1] = Node(2)
    arr[1].next = Node(4)
    arr[1].next.next = Node(6)
    arr[1].next.next.next = Node(8)

    arr[2] = Node(0)
    arr[2].next = Node(9)
    arr[2].next.next = Node(10)
    arr[2].next.next.next = Node(11)

    head = mergeKLists(arr)

    printList(head)