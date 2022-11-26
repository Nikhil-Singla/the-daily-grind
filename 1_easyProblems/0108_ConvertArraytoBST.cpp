/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    TreeNode* sortedArrayToBST(vector<int>& nums) 
    {
        return convert(nums, 0, nums.size()-1);
    }
    TreeNode* convert(vector<int>& nums, int left_index, int right_index)
    {
        if(left_index > right_index)
        {
            return nullptr;
        }
        int mid = (left_index+right_index)/2;
        TreeNode* temp = new TreeNode(nums[mid]);
        temp->left = convert(nums, left_index, mid-1);
        temp->right = convert(nums, mid+1, right_index);
        return temp;
    }
};