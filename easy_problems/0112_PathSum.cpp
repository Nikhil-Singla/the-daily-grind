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
    bool hasPathSum(TreeNode* root, int targetSum) {
        if(root == nullptr)
        {return false;}
        if(targetSum < 0)
        {
            if(root->val < 0)
            {targetSum -= root->val;}
            if(root->val > 0)
            {targetSum += root->val;}
        }
        else
        {
            if(root->val < 0)
            {targetSum += root->val;}
            if(root->val > 0)
            {targetSum -= root->val;}
        }
        if(root->left == nullptr && root->right == nullptr && targetSum == 0)
        {return true;}
        return (hasPathSum(root->left, targetSum) || hasPathSum(root->right, targetSum));
    }
};
