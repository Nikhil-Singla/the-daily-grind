/*
Leetcode problem 144: Binary Tree Preorder Traversal

Problem statement: Given the root of a binary tree, return the preorder traversal of its nodes' values.

Solution approach: Preorder traversal means visiting the current node first, then its left subtree, and finally its right subtree. 
We can implement this using a recursive approach. First, we create a vector to store the values of the nodes in the order that we visit 
them. Then, we define a helper function that takes a TreeNode pointer as input and performs the preorder traversal. If the current node 
is null, we return. Otherwise, we add its value to the vector, and then recursively call the helper function on its left and right 
subtrees (if they exist).

*/

class Solution {
public:
    vector<int> res; // Vector to store the preorder traversal of the tree

    vector<int> preorderTraversal(TreeNode* root) // Function to retrieve the preorder traversal of a binary tree
    {
        res.clear(); // Clear the vector in case it was used previously
        helper(root); // Call the helper function to perform the preorder traversal
        return res; // Return the resulting vector
    }

    void helper(TreeNode* root) // Helper function to perform the preorder traversal
    {
        if(!root) // If the current node is null, return
        {
            return;
        }
        res.push_back(root->val); // Add the value of the current node to the vector
        if(root->left) // If the current node has a left subtree, recursively call the helper function on it
        {
            helper(root->left);
        }    
        if(root->right) // If the current node has a right subtree, recursively call the helper function on it
        {
            helper(root->right);
        }
    }
};


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
