/*Rotate Deque By K

You are given a deque dq (double-ended queue) containing non-negative integers, along with two positive integer type and k. The task is to rotate the deque circularly by k positions.
There are two types of rotation operations:
Right Rotation (Clockwise): If type = 1, rotate the deque to the right. This means moving the last element to the front, and repeating the process k times.
Left Rotation (Anti-Clockwise): If type = 2, rotate the deque to the left. This means moving the first element to the back, and repeating the process k times.

Examples:
Input: dq = [1, 2, 3, 4, 5, 6], type = 1, k = 2
Output: [5, 6, 1, 2, 3, 4] 
Explanation: The type is 1 and k is 2. So, we need to right rotate dequeue by 2 times.
In first right rotation we get [6, 1, 2, 3, 4, 5].
In second right rotation we get [5, 6, 1, 2, 3, 4].

Input: dq = [10, 20, 30, 40, 50], type = 2, k = 3 
Output: [40, 50, 10, 20, 30] 
Explanation: The type is 2 and k is 3. So, we need to left rotate dequeue by 3 times.
In first left rotation we get [20, 30, 40, 50, 10]. 
In second left rotation we get [30, 40, 50, 10, 20].
In third left rotation we get [40, 50, 10, 20, 30].
Constraints:
1 ≤ dq.size() ≤ 105 
1 ≤ k ≤ 105 
1 ≤ type ≤ 2 

Expected Complexities
Time Complexity: O(n)
Auxiliary Space: O(1)*/


import java.util.ArrayDeque;
import java.util.Deque;
public class potd_26sep2025{
   public static void rotateDeque(Deque<Integer> dq, int type, int k) {
        // code here
        int n=dq.size();
        k=k%n;
        if(type==1){
            for(int i=0;i<k;i++){
                dq.addFirst(dq.removeLast());
            }
        }else if(type==2){
            for(int i=0;i<k;i++){
                dq.addLast(dq.removeFirst());
            }
        }
    }
    public static void main(String[] args) {
        Deque<Integer> dq1 = new ArrayDeque<>();
        dq1.add(1);
        dq1.add(2);
        dq1.add(3);
        dq1.add(4);
        dq1.add(5);

        System.out.println("Original Deque 1 (Right Rotation): " + dq1);
        rotateDeque(dq1, 1, 2); // Rotate right by 2
        System.out.println("Deque 1 after right rotation by 2: " + dq1);
    }
}