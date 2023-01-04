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
#include <numeric>
class Solution {
public:
    vector<double> averageOfLevels(TreeNode* root) 
    {
        vector<double> result;
        queue<TreeNode*> q;
        q.push(root);
        while(!q.empty())
        {
            uint const n = q.size();
            long avg = 0;
            for(uint i = 0; i < n; i++)
            {
                TreeNode* temp = q.front();
                q.pop();
                avg += (temp->val);
                if(temp->left)
                {
                    q.push(temp->left);
                }
                if(temp->right)
                {
                    q.push(temp->right);
                }
            }
            result.push_back(avg*1.0/n);
        }
        return result;
    }
};

// First, Brute force approach
class Solution {
public:

    unordered_map<uint, vector<int>> map;
    uint max;

    double getAverage(vector<int> const& v)
    {
        if (v.empty()) 
        {
            return 0;
        }
        double avg = 0, t = 1;
        for(double const c : v)
        {
            avg += (c - avg)/t++;
        }
        return avg;
    }

    vector<double> averageOfLevels(TreeNode* root) 
    {
        max = 0;
        helper(root, 0);  
        vector<double> result;
        for(int i = 0; i <= max; i++)
        {
            result.push_back(getAverage(map[i]));
        }  
        return result;
    }

    void helper(TreeNode* root, uint depth)
    {
        if(depth > max)
        {
            max = depth;
        }
        if(root == NULL)
        {
            return;
        }
        map[depth].push_back(root->val);
        if(root->left)
        {
            helper(root->left, depth+1);
        }
        if(root->right)
        {
            helper(root->right, depth+1);
        }
    }
};