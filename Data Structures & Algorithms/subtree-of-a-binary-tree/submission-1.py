# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # First look for the node
        stack = [root]

        while stack:
            node = stack.pop(0)
            if node.val == subRoot.val:
                if self.isSame(node, subRoot):
                    return True

            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return False
    
    def isSame(self, node1, node2):
        if not node1 or not node2:
            return node1 == node2
        if node1.val != node2.val:
            return False
        return self.isSame(node1.left, node2.left) and self.isSame(node1.right, node2.right)