''''All Unique Permutations of an array

Given an array arr[] that may contain duplicates. Find all possible distinct permutations of the array in sorted order.
Note: A sequence A is greater than sequence B if there is an index i for which Aj = Bj for all j<i and Ai > Bi.

Examples:
Input: arr[] = [1, 3, 3]
Output: [[1, 3, 3], [3, 1, 3], [3, 3, 1]]
Explanation: These are the only possible distinct permutations for the given array.

Input: arr[] = [2, 3]
Output: [[2, 3], [3, 2]]
Explanation: These are the only possible distinct permutations for the given array.
Constraints:
1 ≤ arr.size() ≤ 9
Expected Complexities
Time Complexity: O(n! * n)
Auxiliary Space: O(n)'''

from itertools import permutations
from typing import List
class Solution:
    def uniquePerms(self, arr):
        # code here 
        # 1. itertools.permutations generates all possible permutations, including duplicates.
        #    For an input like [1, 1, 2], it will produce (1, 1, 2) twice.
        all_perms_iterator = permutations(arr)
        
        # 2. Placing the results into a set automatically removes any duplicates.
        #    The set will contain unique tuples, e.g., {(1, 1, 2), (1, 2, 1), (2, 1, 1)}.
        unique_perms_set = set(all_perms_iterator)
        
        # 3. Convert the set of tuples into a list of lists.
        #    We sort the final list to ensure a consistent, predictable output order.
        result = sorted([list(p) for p in unique_perms_set])
        
        return result