# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        p.val, q.val = min(p.val, q.val), max(p.val, q.val)
        if root.val > p.val and root.val < q.val or root.val == p.val or root.val == q.val:
            return root
        
        elif p.val < root.val and q.val < root.val:
            lca = self.lowestCommonAncestor(root.left, p, q)

        else:
            lca = self.lowestCommonAncestor(root.right, p, q)
        
        return lca