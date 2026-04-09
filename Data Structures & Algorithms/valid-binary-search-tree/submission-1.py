# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, minN = -sys.maxsize, maxN = sys.maxsize):
            if not node:
                return True
            val = node.val
            if val <= minN or val >= maxN:
                return False
            left = dfs(node.left, minN, node.val)
            right = dfs(node.right, node.val, maxN)
            return left and right

        return dfs(root)
