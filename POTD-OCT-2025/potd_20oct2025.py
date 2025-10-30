'''Number of BST From Array
You are given an integer array arr[] containing distinct elements.
Your task is to return an array where the ith element denotes the number of unique BSTs formed when arr[i] is chosen as the root.

Examples :
Input: arr[] = [2, 1, 3]
Output: [1, 2, 2]

Input: arr[] = [2, 1]
Ouput: [1, 1]

Constraints:
1 ≤ arr.size() ≤ 6
1 ≤ arr[i] ≤ 15

Expected Complexities
Time Complexity: O(n log n)
Auxiliary Space: O(n)
'''
class Solution:
    bsts=[1,1,2,5,14,42]
    def countBSTs(self, arr):
        # Code here
        n=len(arr)
        l=[]
        for i in range(n):
            x=0
            c=0
            for j in range(n):
                if arr[i]<arr[j]:
                    c+=1
                elif arr[i]>arr[j]:
                    x+=1
            l.append(self.bsts[x]*self.bsts[c])
        return l