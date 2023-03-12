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
    int depth;
    int result;
    int deepestLeavesSum(TreeNode* root) {
        if(root->left==nullptr && root->right==nullptr)
        {
            return root->val;
        }
        depth = 0;
        maxDepth(root, 0);
        result = 0;
        sum(root, 0);
        return result;
    }

    void sum(TreeNode* root, int curr)
    {
        curr += 1;
        if(root->left != nullptr)
        {
            sum(root->left, curr);
        }
        if(root->right != nullptr)
        {
            sum(root->right, curr);
        }
        if(curr == depth)
        {
            result += root->val;
        }
    }

    void maxDepth(TreeNode* root, int deep){
        deep += 1;
        if(root->left != nullptr)
        {
            maxDepth(root->left, deep);
        }
        if(root->right != nullptr)
        {
            maxDepth(root->right, deep);
        }
        if(depth < deep)
        {
            depth = deep;
        }
    }
};