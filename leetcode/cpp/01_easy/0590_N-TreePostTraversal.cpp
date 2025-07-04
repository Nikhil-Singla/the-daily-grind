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

    vector<int> postorder(Node* r) 
    { 
        vector<int> a;
        helper(r, a);    
        return a;
    }

    void helper(Node* r, vector<int> &a)
    {
        if(!r) return;
        for(Node* const c : r->children) {helper(c, a);}
        a.push_back(r->val);
    }
};
