# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxsum = float("-inf")
            
        def helper(node):
            nonlocal maxsum
            if not node:
                return 0
            
            if node.left:
                left_sum = helper(node.left)
            else:
                left_sum = 0
            if node.right:
                right_sum = helper(node.right)
            else:
                right_sum = 0
            maxsum = max(maxsum, node.val + max(0, left_sum) + max(0, right_sum))

            return node.val + max(max(0, left_sum), max(0, right_sum))
        helper(root)

        return maxsum