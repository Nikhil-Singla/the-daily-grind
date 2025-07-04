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
    bool isSameTree(TreeNode* p, TreeNode* q) {
        if((p==nullptr)^(q==nullptr))
        {return false;}
        if(p == nullptr)
        {return true;}
        if(p->val != q->val)
        {return false;}
        if(p->left!=nullptr && q->left!=nullptr)   
        {
            if(!isSameTree(p->left, q->left))
            {return false;}
        }
        else
        {
            if((p->left==nullptr)^(q->left==nullptr))
            {return false;}
        }
        if(p->right!=nullptr && q->right!=nullptr)   
        {
            if(!isSameTree(p->right, q->right))
            {return false;}
        }
        else
        {
            if((p->right==nullptr)^(q->right==nullptr))
            {return false;}
        }
        return true;
    }
};
