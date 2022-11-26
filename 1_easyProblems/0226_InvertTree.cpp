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
    TreeNode* invertTree(TreeNode* root) 
    {
        invert(root);
        return root;
    }
    void invert(TreeNode* root)
    {
        if(root == nullptr)
        {
            return;
        }
        if(root->left != nullptr && root->right != nullptr)
        {
            swap(root->left, root->right);
        }
        if(root->left != nullptr)
        {
            invert(root->left);
        }
        if(root->right != nullptr)
        {
            invert(root->right);
        }
    }
};