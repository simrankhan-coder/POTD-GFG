'''Longest Bounded-Difference Subarray

Given an array of positive integers arr[] and a non-negative integer x, the task is to find the longest sub-array where the absolute difference between any two elements is not greater than x.
If multiple such subarrays exist, return the one that starts at the smallest index.

Examples:

Input: arr[] = [8, 4, 5, 6, 7], x = 3 
Output: [4, 5, 6, 7] 
Explanation: The sub-array described by index [1..4], i.e. [4, 5, 6, 7]
contains no two elements whose absolute differnce is greater than 3.

Input: arr[] = [1, 10, 12, 13, 14], x = 2 
Output: [12, 13, 14] 
Explanation: The sub-array described by index [2..4], i.e. [12, 13, 14]
contains no two elements whose absolute differnece is greater than 2. 
Constraints:
1 ≤ arr.size() ≤ 105
1 ≤ arr[i] ≤ 109
0 ≤ x ≤ 109
Expected Complexities
Time Complexity: O(n)
Auxiliary Space: O(n)
'''
class Solution:
    def longestSubarray(self, arr, x):
        #code here
        minQueue = deque()
        maxQueue = deque()
        n = len(arr)
        start = end = 0
        resStart = resEnd = 0
        while end < n:
            while minQueue and arr[minQueue[-1]] > arr[end]:
                minQueue.pop()
            while maxQueue and arr[maxQueue[-1]] < arr[end]:
                maxQueue.pop()
            minQueue.append(end)
            maxQueue.append(end)
            while arr[maxQueue[0]] - arr[minQueue[0]] > x:
                if start == minQueue[0]:
                    minQueue.popleft()
                if start == maxQueue[0]:
                    maxQueue.popleft()
                start += 1
            if end - start > resEnd - resStart:
                resStart, resEnd = start, end
            end += 1
        return arr[resStart:resEnd+1]