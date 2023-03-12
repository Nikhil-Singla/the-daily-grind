// MUCH BETTER: Iterative Solution
class Solution {
public:
    int fib(int n) 
    {
        vector<int> ans;
        if(n < 2)
        {
            return n;
        }
        ans.push_back(0);
        ans.push_back(1);
        for(int i = 2; i <= n; i++)
        {
            ans.push_back(ans[i-1] + ans[i-2]);
        }
        return ans[n];
    }
};

// Recursive Solution
class Solution {
public:
    int fib(int n) 
    {
        if(n == 0) return 0;
        if(n == 1) return 1;
        return(fib(n-1) + fib(n-2));    
    }
};