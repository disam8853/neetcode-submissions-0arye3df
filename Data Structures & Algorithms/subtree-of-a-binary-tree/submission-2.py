# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(node1, node2):
            if not node1 and node2 or node1 and not node2:
                return False
            if not node1 and not node2:
                return True
            left, right = isSameTree(node1.left, node2.left), isSameTree(node1.right, node2.right)
            return left and right and node1.val == node2.val
        def dfs(node):
            if not node:
                return False
            if isSameTree(node, subRoot):
                return True
            left, right = dfs(node.left), dfs(node.right)
            return left or right
        return dfs(root)