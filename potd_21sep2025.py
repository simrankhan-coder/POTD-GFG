'''Max rectangle
You are given a 2D binary matrix mat[ ][ ], where each cell contains either 0 or 1. Your task is to find the maximum area of a rectangle that can be formed using only 1's within the matrix.

Examples:
Input: mat[][] = [[0, 1, 1, 0],
                [1, 1, 1, 1],
                [1, 1, 1, 1],
                [1, 1, 0, 0]]
Output: 8
Explanation: The largest rectangle with only 1’s is from (1, 0) to (2, 3) which is
[1, 1, 1, 1]
[1, 1, 1, 1]
and area is 4 * 2 = 8.

Input: mat[][] = [[0, 1, 1],
                [1, 1, 1],
                [0, 1, 1]]
Output: 6
Explanation: The largest rectangle with only 1’s is from (0, 1) to (2, 2) which is
[1, 1]
[1, 1]
[1, 1]
and area is 2 * 3 = 6.

Constraints:
1 ≤ mat.size(), mat[0].size() ≤1000
0 ≤ mat[][] ≤1

Expected Complexities
Time Complexity: O(n * m)
Auxiliary Space: O(m)'''


def getMaxArea(heights):
    n = len(heights)
    s = []
    res = 0

    for i in range(n):
    
        # Process all bars that are higher or equal to current
        while s and heights[s[-1]] >= heights[i]:
            tp = s.pop()

            # Width between previous smaller (stack top) and current index
            width = i if not s else i - s[-1] - 1

            res = max(res, heights[tp] * width)
        s.append(i)

    # Process remaining bars in stack
    while s:
        tp = s.pop()
        width = n if not s else n - s[-1] - 1
        res = max(res, heights[tp] * width)

    return res


# Function to find the maximum area of rectangle
# in a 2D matrix.
def maxArea(mat):
    n, m = len(mat), len(mat[0])

    # heights will store histogram heights
    heights = [0] * m
    ans = 0

    for i in range(n):
        for j in range(m):
    
            # Update histogram heights
            if mat[i][j] == 1:
                heights[j] += 1
            else:
                heights[j] = 0
        ans = max(ans, getMaxArea(heights))

    return ans


if __name__ == "__main__":
    mat = [
        [0,1,1,0],
        [1,1,1,1],
        [1,1,1,1],
        [1,1,0,0]
    ]
    print(maxArea(mat))