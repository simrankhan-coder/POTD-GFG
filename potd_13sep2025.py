'''Minimum Cost to cut a board into squares
Given a board of dimensions n × m that needs to be cut into n*m squares. The cost of making a cut along a horizontal or vertical edge is provided in two arrays:

x[]: Cutting costs along the vertical edges (length-wise).
y[]: Cutting costs along the horizontal edges (width-wise).
Find the minimum total cost required to cut the board into squares optimally.

Examples:
Input: n = 4, m = 6, x[] = [2, 1, 3, 1, 4], y[] = [4, 1, 2]
Output: 42
Explanation:
Initially no. of horizontal segments = 1 & no. of vertical segments = 1.
Optimal way to cut into square is:
• Pick 4 (from x) -> vertical cut, Cost = 4 × horizontal segments = 4,
  Now, horizontal segments = 1, vertical segments = 2.
• Pick 4 (from y) -> horizontal cut, Cost = 4 × vertical segments = 8,
  Now, horizontal segments = 2, vertical segments = 2.
• Pick 3 (from x) -> vertical cut, Cost = 3 × horizontal segments = 6,
  Now, horizontal segments = 2, vertical segments = 3.
• Pick 2 (from x) -> vertical cut, Cost = 2 × horizontal segments = 4,
  Now, horizontal segments = 2, vertical segments = 4.
• Pick 2 (from y) -> horizontal cut, Cost = 2 × vertical segments = 8,
  Now, horizontal segments = 3, vertical segments = 4.
• Pick 1 (from x) -> vertical cut, Cost = 1 × horizontal segments = 3,
  Now, horizontal segments = 3, vertical segments = 5.
• Pick 1 (from x) -> vertical cut, Cost = 1 × horizontal segments = 3,
  Now, horizontal segments = 3, vertical segments = 6.
• Pick 1 (from y) -> horizontal cut, Cost = 1 × vertical segments = 6,
  Now, horizontal segments = 4, vertical segments = 6.
So, the total cost = 4 + 8 + 6 + 4 + 8 + 3 + 3 + 6 = 42.

Input: n = 4, m = 4, x[] = [1, 1, 1], y[] = [1, 1, 1]
Output: 15
Explanation: 
Initially no. of horizontal segments = 1 & no. of vertical segments = 1.
Optimal way to cut into square is: 
• Pick 1 (from y) -> horizontal cut, Cost = 1 × vertical segments = 1,
  Now, horizontal segments = 2, vertical segments = 1.
• Pick 1 (from y) -> horizontal cut, Cost = 1 × vertical segments = 1,
  Now, horizontal segments = 3, vertical segments = 1.
• Pick 1 (from y) -> horizontal cut, Cost = 1 × vertical segments = 1,
  Now, horizontal segments = 4, vertical segments = 1.
• Pick 1 (from x) -> vertical cut, Cost = 1 × horizontal segments = 4,
  Now, horizontal segments = 4, vertical segments = 2.
• Pick 1 (from x) -> vertical cut, Cost = 1 × horizontal segments = 4,
  Now, horizontal segments = 4, vertical segments = 3.
• Pick 1 (from x) -> vertical cut, Cost = 1 × horizontal segments = 4,
  Now, horizontal segments = 4, vertical segments = 4
So, the total cost = 1 + 1 + 1 + 4 + 4 + 4 = 15.

Constraints:
2 ≤ n, m ≤ 103
1 ≤ x[i], y[j] ≤103

Time Complexity: O(n*logn + m*logm)
Auxiliary Space: O(1)
'''
def minCost(n,m, x, y):
    
    # Sort the cutting costs in ascending order
    x.sort()
    y.sort()

    hCount, vCount = 1, 1
    i, j = len(x) - 1, len(y) - 1
    totalCost = 0
    while i >= 0 and j >= 0:
        
        # Choose the larger cost cut to 
        # minimize future costs
        if x[i] >= y[j]:
            totalCost += x[i] * hCount
            vCount += 1
            i -= 1
        else:
            totalCost += y[j] * vCount
            hCount += 1
            j -= 1

    # Process remaining vertical cuts
    while i >= 0:
        totalCost += x[i] * hCount
        vCount += 1
        i -= 1

    # Process remaining horizontal cuts
    while j >= 0:
        totalCost += y[j] * vCount
        hCount += 1
        j -= 1

    return totalCost

if __name__ == "__main__":
    
    n,m = 4, 6
    x = [2, 1, 3, 1, 4]
    y = [4, 1, 2]

    print(minCost(n,m,x, y))