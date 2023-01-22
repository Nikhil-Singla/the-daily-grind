/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> children;

    Node() {}

    Node(int _val) {
        val = _val;
    }

    Node(int _val, vector<Node*> _children) {
        val = _val;
        children = _children;
    }
};
*/
class Solution {
public:

    vector<int> answer;

    vector<int> preorder(Node* root) 
    {
        helper(root);
        return answer;
    }

    void helper(Node* root)
    {
        if(!root)
        {return;}
        answer.push_back(root->val);
        for(auto c : root->children)
        {
            helper(c);
        }
    }
};