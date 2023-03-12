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
    int ans = 0;
    int sumOfLeftLeaves(TreeNode* root) 
    {
        //cout<<root->val<<" ";
        if(root->left != nullptr)
        {
            //cout<<root->val<<" ";
            if(((root->left)->left == nullptr) && ((root->left)->right == nullptr))
            {
                //cout<<root->val<<" ";
                ans += root->left->val;
            }
            sumOfLeftLeaves(root->left);
        } 
        if(root->right!=nullptr)
        {
            sumOfLeftLeaves(root->right);
        }
        return ans;
    }
};
