# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def preorder(root, max_so_far):
            if not root:
                return 0
            
            if root.val >= max_so_far:
                return 1 + preorder(root.left, root.val) + preorder(root.right, root.val)
            else:
                return preorder(root.left, max_so_far) + preorder(root.right, max_so_far)
        return preorder(root, float('-inf'))
            