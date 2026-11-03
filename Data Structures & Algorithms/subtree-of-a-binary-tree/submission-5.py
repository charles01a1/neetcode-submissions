# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        queue = [root]

        # if root == None:
        #     if subRoot != None:
        #         return False
        #     else:
        #         return True

        # if subRoot == None:
        #     return True

        while queue:
            current_node = queue.pop(0)
            if current_node and subRoot and current_node.val == subRoot.val:
                temp = self.compare_tree(current_node, subRoot)
                if temp:
                    return True

            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)

        return False

    def compare_tree(self,root, subtree):

        if root and subtree and root.val == subtree.val:
            return self.compare_tree(root.left, subtree.left) and self.compare_tree(root.right, subtree.right)
            
        if root == None and subtree == None:
            return True

        return False


        
        