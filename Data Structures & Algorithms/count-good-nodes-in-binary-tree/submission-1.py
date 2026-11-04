# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good_nodes = [root.val]

        def dfs(root, max_in_path):
            if root.left:
                if root.left.val >= max_in_path:
                    good_nodes.append(root.left.val)
                dfs(root.left,max(max_in_path, root.left.val))

            if root.right:
                if root.right.val >= max_in_path:
                    good_nodes.append(root.right.val)
                dfs(root.right,max(max_in_path, root.right.val))

        dfs(root,root.val)
        # print(good_nodes)
    
        return len(good_nodes)