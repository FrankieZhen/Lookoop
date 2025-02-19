/**
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its minimum depth = 2.
*/

// 2018-7-11
// 111. Minimum Depth of Binary Tree

// Definition for a binary tree node.
 public class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode(int x) { val = x;}
}
class bbb_easy_Minimum_Depth_of_Binary_Tree {
    public int minDepth(TreeNode root) {
        if (root == null) {
          return 0;
        }
        int l = minDepth(root.left);
        int r = minDepth(root.right);

        if (l == 0) {   // 如果左为空则右最小深度+1
            return r+1;
        }
        if (r == 0) {   // 如果右为空则左最小深度+1
            return l+1;
        }

        return (l<r)? l+1:r+1;
    }

    // 另一种写法
    public int minDepth(TreeNode root) {
        if (root == null) {
          return 0;
        }
        if (root.left == null) 
            return 1 + minDepth(root.right);
        if (root.right == null) 
            return 1 + minDepth(root.left);

        return 1 + Math.min(minDepth(root.left), minDepth(root.right));
    }
}