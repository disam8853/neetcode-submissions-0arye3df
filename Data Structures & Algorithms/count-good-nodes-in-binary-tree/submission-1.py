# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans = 0
        def dfs(node, maxNum):
            nonlocal ans
            if not node:
                return
            if node.val >= maxNum:
                ans += 1
                maxNum = node.val
            dfs(node.left, maxNum)
            dfs(node.right, maxNum)
        dfs(root, -sys.maxsize)
        return ans
