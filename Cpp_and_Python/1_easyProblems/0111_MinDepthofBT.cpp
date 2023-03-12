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
    int minDepth(TreeNode* root) {
        if(root == nullptr)
        {return 0;}
        return minDepth(root, 1);
    }
    int minDepth(TreeNode* child, int depth)
    {
        if(child->left == nullptr && child->right == nullptr)
        {return depth;}
        if(child->right == nullptr)
        {return minDepth(child->left, depth+1);}
        else if(child->left == nullptr)
        {return minDepth(child->right, depth+1);}
        else
        {return min(minDepth(child->left, depth+1), minDepth(child->right, depth+1));}
    }
};
