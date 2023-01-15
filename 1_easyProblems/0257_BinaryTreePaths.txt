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

    vector<string> ans;

    vector<string> binaryTreePaths(TreeNode* root) 
    {
        string path;
        helper(root, path);
        return ans;
    }

    void helper(TreeNode* root, string path)
    {
        if(!root)
        {return;}

        path += to_string(root->val);
        if(root->left)
        {
            path.push_back('-');
            path.push_back('>');
            helper(root->left, path);
            path.pop_back();
            path.pop_back();
        }

        if(root->right)
        {
            path.push_back('-');
            path.push_back('>');           
            helper(root->right, path);
            path.pop_back();
            path.pop_back();
        }

        if(!root->left && !root->right)
        {
            ans.push_back(path);
            path.pop_back();
        }
    }
};