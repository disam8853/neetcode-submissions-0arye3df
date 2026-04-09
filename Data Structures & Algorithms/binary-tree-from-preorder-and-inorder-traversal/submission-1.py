# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        val = preorder[0]
        midIdx = inorder.index(val)
        leftInorder = inorder[:midIdx]
        rightInorder = inorder[midIdx + 1:]
        # print(leftInorder, rightInorder)
        node = TreeNode(val)
        node.left = self.buildTree(preorder[1:midIdx+1], leftInorder)
        node.right = self.buildTree(preorder[midIdx+1:], rightInorder)
        return node