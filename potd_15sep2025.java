/*String stack
You are given two strings pat and tar consisting of lowercase English characters. You can construct a new string s by performing any one of the following operation for each character in pat:
Append the character pat[i] to the string s.
Delete the last character of s (if s is empty do nothing).
After performing operations on every character of pat exactly once, your goal is to determine if it is possible to make the string s equal to string tar.

Examples:
Input: pat = "geuaek", tar = "geek"
Output: true
Explanation: Append the first three characters of pat to s, resulting in s = "geu". Delete the last character for 'a', leaving s = "ge". Then, append the last two characters 'e' and 'k' from pat to s, resulting in s = "geek", which matches tar.

Input: pat = "agiffghd", tar = "gfg"
Output: true
Explanation: Skip the first character 'a' in pat. Append 'g' and 'i' to s, resulting in s = "gi". Delete the last character for 'f', leaving s = "g". Append 'f', 'g', and 'h' to s, resulting in s = "gfgh". Finally, delete the last character for 'd', leaving s = "gfg", which matches tar.

Input: pat = "ufahs", tar = "aus"
Output: false
Explanation: It is impossible to construct the string tar from pat with the given operations.

Constraints:
1 ≤ pat.size(), tar.size() ≤ 105 

Expected Complexities
Time Complexity: O(n + m)
Auxiliary Space: O(1*/
public class potd_15sep2025 {
    public static boolean stringStack(String pat, String tar) {
        int i = pat.length() - 1, j = tar.length() - 1;
        
        while (i >= 0 && j >= 0) {
            
            // If characters don’t match, simulate a deletion 
            // by skipping previous character in 'pat'
            if (pat.charAt(i) != tar.charAt(j)) {
                i -= 2;
            } 
            
            // If characters match, move both pointers
            // to the previous character
            else {
                i--;
                j--;
            }
        }
        
        // If we have successfully matched
        // all characters of 'tar', return true
        return j < 0;
    }
    
    public static void main(String[] args) {
        String pat = "geuaek", tar = "geek";
        if (stringStack(pat, tar))
            System.out.println("true");
        else
            System.out.println("false");
    }
}
