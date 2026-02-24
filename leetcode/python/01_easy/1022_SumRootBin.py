# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    _arr = 0
    
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:

        def helper(node, cur):
            cur *= 2 
            cur += 1*(node.val)
                
            if not node.left and not node.right:
                self._arr += cur

            if node.left:
                helper(node.left, cur)

            if node.right:
                helper(node.right, cur)

            return None

        helper(root, 0)
        return self._arr
