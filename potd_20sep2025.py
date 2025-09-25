'''Longest Subarray Length
Difficulty: MediumAccuracy: 45.14%Submissions: 25K+Points: 4
You are given an array of integers arr[]. Your task is to find the length of the longest subarray such that all the elements of the subarray are smaller than or equal to the length of the subarray.

Examples:
Input: arr[] = [1, 2, 3]
Output: 3
Explanation: The longest subarray is the entire array itself, which has a length of 3. All elements in the subarray are less than or equal to 3.

Input: arr[] = [6, 4, 2, 5]
Output: 0
Explanation: There is no subarray where all elements are less than or equal to the length of the subarray. The longest subarray is empty, which has a length of 0.

Constraints:
1 ≤ arr.size() ≤ 105
1 ≤ arr[i] ≤ 109

Expected Complexities
Time Complexity: O(n)
Auxiliary Space: O(n)'''


class Solution:

  def longestSubarray(self, arr: list[int]) -> int:
    """ solution using a monotonic stack"""
    n = len(arr)
    max_len = 0
    
    # The stack will store indices of the array elements
    stack = []

    # We iterate one past the array's end (n+1) to ensure all elements 
    # remaining in the stack are processed.
    for i in range(n + 1):
      
      # The current element to compare against is arr[i], or infinity at the end.
      # Using infinity ensures any elements left in the stack get popped.
      next_greater_val = arr[i] if i < n else float('inf')
      
      # This is the core of the monotonic stack logic.
      # We pop from the stack as long as the current element is greater
      # than the element at the index on top of the stack.
      while stack and arr[stack[-1]] < next_greater_val:
        
        # This is the value of the element being processed
        current_val = arr[stack[-1]]
        stack.pop()
        
        # Calculate the length of the subarray where 'current_val' is the maximum.
        # The right boundary is `i`, the left boundary is the new stack top.
        length = i if not stack else i - stack[-1] - 1
        
        # Check if this subarray is valid (length >= max_element).
        # Here, the maximum element in this calculated subarray is `current_val`.
        if length >= current_val:
          max_len = max(max_len, length)
          
      # Push the current index onto the stack
      stack.append(i)
      
    return max_len
  
def main():
  # Create an instance of the Solution class
  solver = Solution()

  # Input array as specified
  arr = [1, 2, 3]

  # Call the method to get the result
  result = solver.longestSubarray(arr)

  # Print the input and the final output
  print(f"Input: arr = {arr}")
  print(f"Output: {result}")

if __name__ == "__main__":
  main()