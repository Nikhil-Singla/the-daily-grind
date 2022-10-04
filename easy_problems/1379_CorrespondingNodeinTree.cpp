/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

class Solution {
public:
    TreeNode* result;
    TreeNode* getTargetCopy(TreeNode* original, TreeNode* cloned, TreeNode* target) {
        //Inorder = (Left Value Right)
        //Preorder = (V L R)
        //Postorder = (L R V)
        if(cloned->left!=NULL)
        {getTargetCopy(original->left, cloned->left, target);}
        if(cloned->val == target->val)
        {
            result = cloned;
        }
        if(cloned->right!=NULL)
        {getTargetCopy(original->right, cloned->right, target);}
        return result;
    }
};
