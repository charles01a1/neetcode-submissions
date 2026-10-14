# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        # result = [root]
        queue = [root]

        while queue:
            cur = queue.pop(0)
            if cur:
                if cur.right and cur.left:
                    temp = cur.right
                    cur.right = cur.left
                    cur.left = temp
                
                    queue.append(cur.left)
                    queue.append(cur.right)
                elif cur.right:
                    cur.left = cur.right 
                    cur.right = None
                    queue.append(cur.left)
                elif cur.left:
                    cur.right = cur.left
                    cur.left = None
                    queue.append(cur.right)

            
        return root

        