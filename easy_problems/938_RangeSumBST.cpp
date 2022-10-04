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
    //Taken IsBound's concept from Google Search and modified to fit
    int sum;
    Solution()
    {
        sum = 0;
    }
    bool IsBound(const int value, const int low, const int high) 
    {
        return (!(value < low) && !(high < value));
    }
    int rangeSumBST(TreeNode* root, int low, int high) {
        
        if(root->left!=nullptr)
        {rangeSumBST(root->left, low, high);}

        if(IsBound(root->val,low,high))
        {
            cout<<root->val<<" ";
            sum+=root->val;
        }

        if(root->right!=nullptr)
        {rangeSumBST(root->right, low, high);}
        return sum;
    }
};
