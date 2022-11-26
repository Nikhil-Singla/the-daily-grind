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

    vector<int> getOrder;

    void flatten(TreeNode* root) 
    {
        if(root==NULL || root->left==NULL && root->right==NULL)
        {
            return;
        }
        traverse(root);
        root->left = NULL;
        root->right = NULL;
        for(int i = 1; i < getOrder.size(); i++)
        {
            TreeNode *newNode = new TreeNode(getOrder[i]);    
            root->right = newNode;   
            root = newNode;
        }

    }


};