/*Remove BST keys outside given range
Given the root of a Binary Search Tree (BST) and two integers l and r, remove all the nodes whose values lie outside the range [l, r].
Note: The modified tree should also be BST and the sequence of the remaining nodes should not be changed.

Examples:
Input: root = [6, -13, 14, N, -8, 13, 15, N, N, 7], l = -10, r = 13
Output: [6, -8, 13, N, N, 7]
Explanation: All the nodes outside the range [-10, 13] are removed and the modified tree is a valid BST.

Input: root = [14, 4, 16, 2, 8, 15, N, -8, 3, 7, 10], l = 2, r = 6
 Output: [4, 2, N, N, 3]
Explanation: All the nodes outside the range [2, 6] are removed and the modified tree is a valid BST.
  
Constraints:
1 ≤ number of nodes ≤ 104
1 ≤ node->data ≤ 104
1 ≤ l ≤ r ≤ 104

Expected Complexities
Time Complexity: O(n)
Auxiliary Space: O(n)
 */
public class potd_16oct2025 {
    
class Node {
    int data;
    Node left;
    Node right;
    Node(int data){
        this.data = data;
        left=null;
        right=null;
    }
}


class Solution {
    Node removekeys(Node root, int l, int r) {
        // code here
        if (root == null)
            return null;
        Node left = removekeys(root.left, l, r);
        Node right = removekeys(root.right, l, r);

        // If curr node lies in the range, update its
        // left and right nodes and return curr node.
        if (root.data >= l && root.data <= r) {
            root.left = left;
            root.right = right;

            return root;
        }

        // If current node is less than range,
        // then return the updated right subtree.
        else if (root.data < l) {
            return right;
        }

        // Else return the updated left subtree.
        else {
            return left;
        }
    }
}
}
