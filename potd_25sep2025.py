'''Generate Binary Numbers
Given a number n. The task is to generate all binary numbers with decimal values from 1 to n.

Examples:
Input: n = 4
Output: ["1", "10", "11", "100"]
Explanation: Binary numbers from 1 to 4 are 1, 10, 11 and 100.

Input: n = 6
Output: ["1", "10", "11", "100", "101", "110"]
Explanation: Binary numbers from 1 to 6 are 1, 10, 11, 100, 101 and 110.
Constraints:
1 ≤ n ≤ 106

Expected Complexities
Time Complexity: O(n)
Auxiliary Space: O(n)'''

from collections import deque

def generateBinary(n):
    res = []
    q = deque()

    # Enqueue the first binary number
    q.append("1")

    # This loop is like BFS of a tree with 1 as root
    # 0 as left child and 1 as right child and so on
    while n > 0:
        # print the front of queue
        s1 = q.popleft()
        res.append(s1)

        s2 = s1
        
        if len(q) < n:

            # Append "0" to s1 and enqueue it.
            q.append(s1 + "0")
    
            # Append "1" to s2 and enqueue it.
            q.append(s2 + "1")

        n -= 1

    return res

if __name__ == "__main__":
    n = 6
    res = generateBinary(n)
    for i in res:
        print(i, end=" ")
    print()