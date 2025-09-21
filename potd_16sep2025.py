'''Postfix Evaluation
You are given an array of strings arr[] that represents a valid arithmetic expression written in Reverse Polish Notation (Postfix Notation). Your task is to evaluate the expression and return an integer representing its value.
Note: A postfix expression is of the form operand1 operand2 operator (e.g., "a b +"). 
And the division operation between two integers always computes the floor value, i.e floor(5 / 3) = 1 and floor(-5 / 3) = -2.
It is guaranteed that the result of the expression and all intermediate calculations will fit in a 32-bit signed integer.

Examples:
Input: arr[] = ["2", "3", "1", "*", "+", "9", "-"]
Output: -4
Explanation: If the expression is converted into an infix expression, it will be 2 + (3 * 1) – 9 = 5 – 9 = -4.

Input: arr[] = ["2", "3", "^", "1", "+"]
Output: 9
Explanation: If the expression is converted into an infix expression, it will be 2 ^ 3 + 1 = 8 + 1 = 9.

Constraints:
3 ≤ arr.size() ≤ 103
arr[i] is either an operator: "+", "-", "*", "/" or "^", or an integer in the range [-104, 104]

Expected Complexities
Time Complexity: O(n)
Auxiliary Space: O(n)'''
import math

def evaluatePostfix(arr):
    st = []

    for token in arr:
        
        # If it's an operand (number), push it onto the stack
        if token[0].isdigit() or (len(token) > 1 and token[0] == '-'):
            st.append(int(token))
        
        # Otherwise, it must be an operator
        else:
            val1 = st.pop()
            val2 = st.pop()

            if token == '+':
                st.append(val2 + val1)
            elif token == '-':
                st.append(val2 - val1)
            elif token == '*':
                st.append(val2 * val1)
            elif token == '/':
                st.append(val2 // val1)
            elif token == '^':
                st.append(int(math.pow(val2, val1)))
    return st.pop()

if __name__ == '__main__':
    arr = ["2", "3", "1", "*", "+", "9", "-"]
    print(evaluatePostfix(arr))