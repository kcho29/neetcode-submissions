# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        lca = None
        def dfs(node, p, q):
            nonlocal lca
            if not node:
                return False
            nodeis = node.val == p.val or node.val == q.val

            leftcontains = dfs(node.left, p, q)
            rightcontains = dfs(node.right, p, q)

            if nodeis + leftcontains + rightcontains == 2:
                lca = node
            return nodeis or leftcontains or rightcontains
        dfs(root,p,q)
        return lca
