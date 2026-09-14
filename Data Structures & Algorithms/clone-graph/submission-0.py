"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        cloneDict = {}

        def dfs(n):
            if n in cloneDict:
                return cloneDict[n]
            
            newNode = Node(n.val)
            cloneDict[n] = newNode

            for neigh in n.neighbors:
                newNode.neighbors.append(dfs(neigh))
            return newNode
        return dfs(node)
