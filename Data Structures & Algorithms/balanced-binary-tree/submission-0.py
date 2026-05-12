# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        height = self.calculateHeight(root)
        if not height:
            return False
        else:
            return True

    def calculateHeight(self, root):
        if not root:
            return 0
        
        left = self.calculateHeight(root.left)
        right = self.calculateHeight(root.right)

        if left is False or right is False or abs(right - left) > 1:
            return False

        return 1 + max(left, right)