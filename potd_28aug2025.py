"""Maximize Number of 1's

Given a binary array arr[] containing only 0s and 1s and an integer k, you are allowed to flip at most k 0s to 1s. Find the maximum number of consecutive 1's that can be obtained in the array after performing the operation at most k times.

Examples:
Input: arr[] = [1, 0, 1], k = 1
Output: 3
Explanation: By flipping the zero at index 1, we get the longest subarray from index 0 to 2 containing all 1’s.

Input: arr[] = [1, 0, 0, 1, 0, 1, 0, 1], k = 2
Output: 5
Explanation: By flipping the zeroes at indices 4 and 6, we get the longest subarray from index 3 to 7 containing all 1’s.

Input: arr[] = [1, 1], k = 2
Output: 2
Explanation: Since the array is already having the max consecutive 1's, hence we dont need to perform any operation. Hence the answer is 2.
Constraints:

1 ≤ arr.size() ≤ 105
0 ≤ k ≤ arr.size()
0 ≤ arr[i] ≤ 1

Expected Complexities
Time Complexity: O(n)
Auxiliary Space: O(1)
"""
def maxOnes(arr, k):
    res = 0

    # Start and end pointer of the window
    start = 0
    end = 0

    # Counter to keep track of zeros in current window
    cnt = 0

    while end < len(arr):
        if arr[end] == 0:
            cnt += 1

        # Shrink the window from left if no. 
        # of zeroes are greater than k
        while cnt > k:
            if arr[start] == 0:
                cnt -= 1

            start += 1

        res = max(res, (end - start + 1))

        # Increment the end pointer 
        # to expand the window
        end += 1

    return res

#Backend code
if __name__ == "__main__":
    arr = [1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1]
    k = 2
    print(maxOnes(arr, k))
