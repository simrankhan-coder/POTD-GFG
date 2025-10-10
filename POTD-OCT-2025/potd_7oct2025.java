/*Bottom View of Binary Tree
You are given the root of a binary tree, and your task is to return its bottom view. The bottom view of a binary tree is the set of nodes visible when the tree is viewed from the bottom.
Note: If there are multiple bottom-most nodes for a horizontal distance from the root, then the latter one in the level order traversal is considered.

Examples :
Input: root = [1, 2, 3, 4, 5, N, 6]
    Output: [4, 2, 5, 3, 6]
Explanation: The Green nodes represent the bottom view of below binary tree.
    
Input: root = [20, 8, 22, 5, 3, 4, 25, N, N, 10, 14, N, N, 28, N]
    Output: [5, 10, 4, 28, 25]
Explanation: The Green nodes represent the bottom view of below binary tree.
    
Constraints:
1 ≤ number of nodes ≤ 105
1 ≤ node->data ≤ 105 

Expected Complexities
Time Complexity: O(n)
Auxiliary Space: O(n)*/
import java.util.ArrayList;
import java.util.Queue;
import java.util.TreeMap;
import java.util.LinkedList;


public class potd_7oct2025 {
class Node {
    int data;
    Node left, right;

    Node(int x) {
        data = x;
        left = right = null;
    }
}
class Pair{
    int hd;
    Node node;
    Pair(Node node,int hd){
        this.node=node;
        this.hd=hd;
    }
}
class Solution {
    public ArrayList<Integer> bottomView(Node root) {
        // Code here
        ArrayList<Integer> arr=new ArrayList<>();
        if(root==null){
            return arr;
        }
        TreeMap<Integer,Integer> map=new TreeMap<>();
        Queue<Pair> q=new LinkedList<>();
        q.add(new Pair(root,0));
        while(!q.isEmpty()){
            Pair curr=q.poll();
            Node node=curr.node;
            int hd=curr.hd;
            map.put(hd,node.data);
            if(node.left!=null){
                q.add(new Pair(node.left,hd-1));
            }
            if(node.right!=null){
                q.add(new Pair(node.right,hd+1));
            }
        }
        for(int data:map.values()){
            arr.add(data);
        }
        return arr;
    }
}
    
}
