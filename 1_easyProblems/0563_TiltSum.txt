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

    int Tilt = 0;

    int findTilt(TreeNode* root) 
    {
        helper(root);
        return Tilt;
    }

    int helper(TreeNode* root)
    {
        if(!root) {return 0;}
        int leftSum = helper(root->left);
        int rightSum = helper(root->right);
        Tilt += abs(leftSum - rightSum);
        return leftSum + rightSum + root -> val;
    }
};