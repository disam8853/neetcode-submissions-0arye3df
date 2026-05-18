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
            return node
        mp = {}

        def dfs(node):
            curNode = Node(node.val)
            mp[node.val] = curNode
            for n in node.neighbors:
                if n.val in mp:
                    curNode.neighbors.append(mp[n.val])
                    continue
                newNode = dfs(n)
                curNode.neighbors.append(newNode)
            return curNode

        return dfs(node)