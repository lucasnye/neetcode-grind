# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k
        def dfs(root, k):
            if not root:
                return 0

            left = dfs(root.left, k)
            self.k -= 1
            if self.k == 0:
                return root.val
            right = dfs(root.right, k)
            return 0 + left + right
        
        return dfs(root, k)
            