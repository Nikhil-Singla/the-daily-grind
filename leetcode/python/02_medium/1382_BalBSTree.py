# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    _array = []
    
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Need to re-init because leetcode uses the same class
        self._array = []
        
        self.traverse(root)
        
        new_root = self.make_tree(self._array)
        return new_root

    def make_tree(self, input_array):
        # input_array = List in Python
        if not bool(input_array):
            return None
            
        n = len(input_array)
        if n == 1:
            return TreeNode(input_array[0], None, None)

        mid = n // 2
        # a = [1, 2]
        # print(a[2:]) => []

        node = TreeNode(input_array[mid], self.make_tree(input_array[:mid]), self.make_tree(input_array[mid+1:]))

        return node

    def traverse(self, root):
        if root.left:
            self.traverse(root.left)

        if root.val:
            self._array.append(root.val)

        if root.right:
            self.traverse(root.right)
