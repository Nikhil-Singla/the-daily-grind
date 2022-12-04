//ITERATIVE Solution
class Solution {
public:
    int tribonacci(int n) 
    {
        vector<int> ans;
        ans.push_back(0);
        ans.push_back(1);
        ans.push_back(1);
        for(auto i = 3; i <= n; i++)
        {
            ans.push_back(ans[i-1] + ans[i-2] + ans[i-3]);
        }    
        return ans[n];
    }
};

// RECURSIVE Solution (failed due to time limit 35/39)
class Solution {
public:
    int tribonacci(int n) 
    {
        if (n == 0) return 0;
        if (n == 1) return 1;
        if (n == 2) return 1;
        return tribonacci(n-1) + tribonacci(n-2) + tribonacci(n-3);
    }
};