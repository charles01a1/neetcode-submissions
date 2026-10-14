# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def dfs(root, depth):
            if root == None:
                return 0
            
            if root.right == None and root.left == None:
                return depth + 1
            
            if root.right or root.left:
                return 1 + max(dfs(root.right, depth), dfs(root.left, depth))

        return dfs(root,0)    