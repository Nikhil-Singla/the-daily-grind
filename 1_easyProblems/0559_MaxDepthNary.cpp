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

    int max = 0;

    int maxDepth(Node* root) 
    {
        if(!root) {return 0;}
        helper(root, 1);
        return max;
    }

    void helper(Node* root, int depth)
    {
        if(max < depth) {max = depth;}
        for(auto c : root->children)
        {
            helper(c, depth+1);
        }
    }
};