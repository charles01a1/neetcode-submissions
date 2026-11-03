# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        in_order = []

        def dfs(root):
            if not root.left and not root.right:
                in_order.append(root.val)
                return

            if root.left:
                dfs(root.left)

            in_order.append(root.val)

            if root.right:
                dfs(root.right)

        dfs(root)
        return in_order[k-1]