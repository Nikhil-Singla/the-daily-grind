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

    TreeNode* prev = NULL;
    int low;
    int getMinimumDifference(TreeNode* root) 
    {
        low = INT_MAX;
        helper(root);
        return low;
    }

    void helper(TreeNode* root)
    {
        if(!root) {return;}
        if(root->left) {
            helper(root->left);
        }
        if(prev) {low = min(low, root->val - prev->val);}
        prev = root;
        if(root->right) {helper(root->right);}
    }
};