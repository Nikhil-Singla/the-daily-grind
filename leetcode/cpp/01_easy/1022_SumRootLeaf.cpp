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
#include <stdint.h>
#include <math.h>
#include <stack>
class Solution {
public:
    int32_t answer;
    Solution()
    {
        answer = 0;
    }
    int sumRootToLeaf(TreeNode* root) 
    {
        sum(root, 0);
        return answer;
    }
    void sum(TreeNode* root, int power)
    {
        power = (root->val) + (power*2);
        if(root->right==nullptr && root->left==nullptr)
        {   
            answer += power;
            return;
        }
        if(root->left!=nullptr)
        {
            sum(root->left,power);
        }
        if(root->right!=nullptr)
        {
            sum(root->right,power);
        }
    }
};
