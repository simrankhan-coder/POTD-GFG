'''Decode the string
Given an encoded string s, decode it by expanding the pattern k[substring], where the substring inside brackets is written k times. k is guaranteed to be a positive integer, and encodedString contains only lowercase english alphabets. Return the final decoded string.
Note: The test cases are generated so that the length of the output string will never exceed 105 .

Examples:
Input: s = "3[b2[ca]]"
Output: "bcacabcacabcaca"
Explanation:
Inner substring “2[ca]” breakdown into “caca”.
Now, new string becomes “3[bcaca]”
Similarly “3[bcaca]” becomes “bcacabcacabcaca” which is final result.

Input: s = "3[ab]"
Output: "ababab"
Explanation: The substring "ab" is repeated 3 times giving "ababab".

Constraints:
1 ≤ |s| ≤ 105 
1 ≤ k ≤ 100

Expected Complexities
Time Complexity: O(n)
Auxiliary Space: O(n)'''

def decodeString(s: str) -> str:
    st = []

    for i in range(len(s)):
        
        # Push characters into the stack until ']' is encountered
        if s[i] != ']':
            st.append(s[i])
            
        # Decode when ']' is found
        else:
            temp = []
            
            # Pop characters until '[' is found
            while st and st[-1] != '[':
                temp.append(st.pop())
            temp.reverse()  
            st.pop()

            num = []
            
            # Extract the number (repetition count) from the stack
            while st and st[-1].isdigit():
                num.insert(0, st.pop())

            # Convert extracted number to integer
            number = int("".join(num))
            repeat = "".join(temp) * number  
            
            # Push the expanded string back onto the stack
            st.extend(repeat)

    # Pop all characters from stack to form the final result
    return "".join(st)

if __name__ == "__main__":
    str_val = "3[b2[ca]]"
    print(decodeString(str_val))