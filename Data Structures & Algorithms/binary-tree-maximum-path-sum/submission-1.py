# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = root.val

        def dfs(node):
            nonlocal ans
            if not node:
                return -sys.maxsize

            res = node.val
            left = dfs(node.left)
            right = dfs(node.right)
            res = max(res, node.val + max(0, left))
            res = max(res, node.val + max(0, right))
            
            ans = max(ans, res, node.val + left + right)

            return res
        dfs(root)
        return ans
