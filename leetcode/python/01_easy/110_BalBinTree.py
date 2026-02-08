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

        if root.left:
            left_height, left_subtree = self.get_data(root.left, 1)
        else:
            left_height, left_subtree = 0, True

        if root.right:
            right_height, right_subtree = self.get_data(root.right, 1)
        else:
            right_height, right_subtree = 0, True

        if not (left_subtree and right_subtree) or abs(left_height - right_height) > 1:
            return False
        else:
            return True

    def get_data(self, node, depth):
        if node.left:
            left_height, left_sub = self.get_data(node.left, depth+1)
        else:
            left_height, left_sub = 0, True

        if node.right:
            right_height, right_sub = self.get_data(node.right, depth+1)
        else:
            right_height, right_sub = 0, True

        if not (right_sub and left_sub) or abs(left_height-right_height) > 1:
            return 0, False
        else:
            return max(left_height, right_height) + 1, True
