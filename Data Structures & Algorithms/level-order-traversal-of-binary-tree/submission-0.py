# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        out = []
        if not root:
            return []
        stack = [(root, 0)]
        curlayer = -1
        while stack:
            node, layer = stack.pop(0)
            # New layer
            if layer != curlayer:
                out.append([node.val])
                curlayer += 1
            else:
                out[-1].append(node.val)
            if node.left:
                stack.append((node.left, curlayer+1))
            if node.right:
                stack.append((node.right, curlayer+1))
        return out