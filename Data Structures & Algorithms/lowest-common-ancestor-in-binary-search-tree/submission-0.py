# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        p, q = p.val, q.val
        node = root
        while node:
            val = node.val
            if val > p and val > q:
                node = node.left
            elif val < p and val < q:
                node = node.right
            elif p < val < q or q < val < p or val == q or val == p:
                return node
        return node