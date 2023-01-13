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
    //vector<int> ar;
    TreeNode *first = nullptr, *second = nullptr, *prev = nullptr;
    void recoverTree(TreeNode* root) 
    {
        helper(root);
        /*int tar1, tar2;
        for(uint i = 0; i < ar.size()-1; i++)
        {
            if(ar[i] >)
        }*/
        swap(first->val, second->val);
    }

    void helper(TreeNode* root)
    {
        if(!root)
        {
            return;
        }
        if(root->left)
        {
            helper(root->left);
        }
        //ar.push_back(root->val);
        
        if(prev && root->val < prev->val)
        {
            if(!first)
            {first=prev;}
            second=root;
        }
        prev=root;

        if(root->right)
        {
            helper(root->right);
        }
    }
};