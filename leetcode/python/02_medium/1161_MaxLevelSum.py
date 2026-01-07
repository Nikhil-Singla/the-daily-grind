# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def helper(self, root, curr_depth, depth_arr):
        if root == None:
            return

        global depth
        if depth_arr[curr_depth] == None:
            depth_arr[curr_depth] = 0
        
        depth_arr[curr_depth] += root.val

        if root.left is not None:
            self.helper(root.left, curr_depth+1, depth_arr)
        
        if root.right is not None:
            self.helper(root.right, curr_depth+1, depth_arr)


    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        depth = [None] * 1001
        self.helper(root, 1, depth)
        max_idx = 1

        max_sum = depth[max_idx]

        for idx, i in enumerate(depth):
            if i is not None: 
                if i > max_sum :
                    max_sum = i
                    max_idx = idx

        return max_idx
