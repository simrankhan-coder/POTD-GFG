/*K closest Values
Given the root of a Binary Search Tree, a target value, and an integer k. Your task is to find the k values in the BST that are closest to the target.
The closest value is taken by choosing the one that gives minimum absolute difference from target.
Note: In case two values have same absolute difference from target, choose the smaller one. The target may or may not be present in BST.
You can return the values in any order the driver code will print them in sorted order only.

Examples:
Input: root = [20, 8, 22, 4, 12, N, N, N, N, 10, 14], target = 17, k = 3
Output: [14, 20, 12]
Explanation: Absolute difference of 17 wrt 14 and 20 is 3 and 3, but we choose the smaller value in case of same absolute difference. So, 14 coes first and then 20. Then, 12 and 22 have same absolute difference, i.e., 5 from 17. But we choose the smaller value, i.e., 12.
     
Input: root = [5, 4, 8, 1], target = 5, k = 2
Output: [5, 4]
Explanation: The absolute difference of 5 wrt 5 is 0, and for 4, the absolute difference is 1.
    
Constraints:
1 ≤ number of nodes, k ≤ 104
1 ≤ node->data, target ≤ 104

Expected Complexities
Time Complexity: O(n)
Auxiliary Space: O(n) */

import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Deque;

public class potd_19oct2025 {
    
class Node {
    int data;
    Node left;
    Node right;

    Node(int data) {
        this.data = data;
        left = null;
        right = null;
    }
}

class Solution {
    public ArrayList<Integer> getKClosest(Node root, int target, int k) {
        // code here
        Deque<Integer>dq=new ArrayDeque<>();
        ArrayList<Integer>ans=new ArrayList<>();
        inorder(root,target,k,dq);
        while(!dq.isEmpty()){
            ans.add(dq.pollFirst());
        }
        return ans;
    }
    public void inorder(Node root,int target,int k,Deque<Integer>dq){
       if(root==null){
           return;
       }
       inorder(root.left,target,k,dq);
       if(dq.size()<k){
           dq.addLast(root.data);
       }else if(Math.abs(dq.peekFirst()-target)>Math.abs(root.data-target)){
           dq.removeFirst();
           dq.addLast(root.data);
       }else{
           return;
       }
       inorder(root.right,target,k,dq);
    }
}
}
