# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        ans = 0
        def dfs(node):
            nonlocal ans
            if not node:
                return -1
            left, right = dfs(node.left), dfs(node.right)
            print(node.val, left + right + 2)
            ans = max(ans, left + right + 2)
            return max(left, right) + 1
        dfs(root)
        return ans