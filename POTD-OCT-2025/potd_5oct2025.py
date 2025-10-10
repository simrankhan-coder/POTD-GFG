'''Rat in a Maze
Consider a rat placed at position (0, 0) in an n x n square matrix maze[][]. The rat's goal is to reach the destination at position (n-1, n-1). The rat can move in four possible directions: 'U'(up), 'D'(down), 'L' (left), 'R' (right).

The matrix contains only two possible values:
0: A blocked cell through which the rat cannot travel.
1: A free cell that the rat can pass through.
Your task is to find all possible paths the rat can take to reach the destination, starting from (0, 0) and ending at (n-1, n-1), under the condition that the rat cannot revisit any cell along the same path. Furthermore, the rat can only move to adjacent cells that are within the bounds of the matrix and not blocked.
If no path exists, return an empty list.
Note: Return the final result vector in lexicographically smallest order.
Examples:

Input: maze[][] = [[1, 0, 0, 0], [1, 1, 0, 1], [1, 1, 0, 0], [0, 1, 1, 1]]
Output: ["DDRDRR", "DRDDRR"]
Explanation: The rat can reach the destination at (3, 3) from (0, 0) by two paths - DRDDRR and DDRDRR, when printed in sorted order we get DDRDRR DRDDRR.

Input: maze[][] = [[1, 0], [1, 0]]
Output: []
Explanation: No path exists as the destination cell (1, 1) is blocked.

Input: maze[][] = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
Output: ["DDRR", "RRDD"]
Explanation: The rat has two possible paths to reach the destination: DDRR and RRDD.
Constraints:
2 ≤ n ≤ 5
0 ≤ maze[i][j] ≤ 1

Expected Complexities
Time Complexity: O(4 ^ (n * n))
Auxiliary Space: O(n * n)'''
class Solution:
    def ratInMaze(self, maze):
        # code here
        n = len(maze)
        m = len(maze[0])
        result = []
        def Traverse(i, j, res):
        # Boundary and block checks
            if i < 0 or j < 0 or i >= n or j >= m or maze[i][j] != 1:
                return
            # Destination reached
            if i == n - 1 and j == m - 1:
                result.append(res)
                return
            # Mark as visited
            maze[i][j] = -1
            # Try all four directions (U, D, L, R)

            Traverse(i - 1, j, res + "U") # Up

            Traverse(i + 1, j, res + "D") # Down

            Traverse(i, j - 1, res + "L") # Left

            Traverse(i, j + 1, res + "R") # Right
            # Backtrack (unmark)
            maze[i][j] = 1
            # Start traversal only if the starting cell is open         
        if maze[0][0] == 1:
            Traverse(0, 0, "")
        return sorted(result)