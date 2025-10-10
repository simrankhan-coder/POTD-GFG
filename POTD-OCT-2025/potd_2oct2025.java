/*Unique K-Number Sum

Given two integers n and k, the task is to find all valid combinations of k numbers that adds up to n based on the following conditions:
Only numbers from the range [1, 9] used.
Each number can only be used at most once.
Note: You can return the combinations in any order, the driver code will print them in sorted order.

Examples:

Input: n = 9, k = 3
Output: [[1, 2, 6], [1, 3, 5], [2, 3, 4]]
Explanation: There are three valid combinations of 3 numbers that sum to 9: [1 ,2, 6], [1, 3, 5] and [2, 3, 4].

Input: n = 3, k = 3
Output: []
Explanation: It is not possible to pick 3 distinct numbers from 1 to 9 that sum to 3, so no valid combinations exist.
Constraints:
1 ≤ n ≤ 50
1 ≤ k ≤ 9 
Expected Complexities
Time Complexity: O(k * 2^9)
Auxiliary Space: O(k)*/
import java.util.ArrayList;
public class potd_2oct2025{
  class Solution {
    public ArrayList<ArrayList<Integer>> combinationSum(int n, int k) {
        // code here
        ArrayList<ArrayList<Integer>> results = new ArrayList<>();
        findCombinations(n, k, new ArrayList<>(), results, 1);
        return results;
    }
    private void findCombinations(int remainingSum, int remainingCount, 
                                  ArrayList<Integer> currentCombo, 
                                  ArrayList<ArrayList<Integer>> results, 
                                  int startNum) {

        // Base case: A valid combination is found
        if (remainingSum == 0 && remainingCount == 0) {
            results.add(new ArrayList<>(currentCombo));
            return;
        }

        // Pruning: Stop if the state is invalid
        if (remainingSum < 0 || remainingCount < 0) {
            return;
        }
        
        // Loop through candidate numbers
        for (int i = startNum; i <= 9; i++) {
            // Choose the current number
            currentCombo.add(i);
            // Recurse with updated state
            findCombinations(remainingSum - i, remainingCount - 1, currentCombo, results, i + 1);

            // Backtrack: Remove the current number to explore other possibilities
            currentCombo.remove(currentCombo.size() - 1);
        }
    }
}  
}
