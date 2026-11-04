# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(root, max_in_path,good_nodes):
            result = good_nodes
            if root.left:
                if root.left.val >= max_in_path:
                    result += 1
                result += dfs(root.left,max(max_in_path, root.left.val),0)

            if root.right:
                if root.right.val >= max_in_path:
                   result += 1
                result += dfs(root.right,max(max_in_path, root.right.val),0)
            
            return result
    
        return dfs(root,root.val,1)