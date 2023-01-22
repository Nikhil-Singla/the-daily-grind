class Solution {
public:

    int maxDepth(Node* root) 
    {
        if(!root) {return 0;}
        int maxD = 1;
        for(auto const c : root->children)
        {
            maxD = max(maxD, 1 + maxDepth(c));
        }
        return maxD;
    }

};

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