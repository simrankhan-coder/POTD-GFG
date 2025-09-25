'''Queue Reversal
Given a queue q containing integer elements, your task is to reverse the queue.

Examples:
Input: q[] = [5, 10, 15, 20, 25]
Output: [25, 20, 15, 10, 5]
Explanation: After reversing the given elements of the queue, the resultant queue will be 25 20 15 10 5.

Input: q[] = [1, 2, 3, 4, 5]
Output: [5, 4, 3, 2, 1]
Explanation: After reversing the given elements of the queue, the resultant queue will be 5 4 3 2 1.

Constraints:
1 ≤ q.size() ≤ 103
0 ≤ q[i] ≤ 105

Expected Complexities
Time Complexity: O(n)
Auxiliary Space: O(n)'''

from collections import deque

def reverseQueue(q):
    st = []
    
    # Transfer all elements from queue to stack
    while q:
        st.append(q[0])
        q.popleft()
    
    # Transfer all elements back from stack to queue
    # This reverses the order
    while st:
        q.append(st.pop())

if __name__ == "__main__":
    q = deque([5, 10, 15, 20, 25])
    
    reverseQueue(q)
    
    while q:
        print(q.popleft(), end=' ')