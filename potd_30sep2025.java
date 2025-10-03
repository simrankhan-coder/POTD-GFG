/*Generate all binary strings

Given an integer n. You need to generate all the binary strings of n characters representing bits.
Note: Return the strings in  ascending order.
Examples:

Input: n = 2
Output: [00, 01, 10, 11]
Explanation: As each position can be either 0 or 1, the total possible combinations are 4.

Input: n = 3
Output: [000, 001, 010, 011, 100, 101, 110, 111]
Explanation: As each position can be either 0 or 1, the total possible combinations are 8.
Constraints:
1 ≤ n ≤ 20 
Expected Complexities
Time Complexity: O(n * 2^n)
Auxiliary Space: O(n)*/
import java.util.*;
class Solution {
    public ArrayList<String> binstr(int n) {
        // code here
         ArrayList<String> res = new ArrayList<>();
        
        for (int i = 0; i < (1 << n); i++) {
            
            StringBuilder s = new StringBuilder();
            
            // build string from bits of i
            for (int j = n - 1; j >= 0; j--)
                s.append(((i >> j) & 1) == 1 ? '1' : '0');
            
            res.add(s.toString());
        }
        
        return res;
        
    }
}
