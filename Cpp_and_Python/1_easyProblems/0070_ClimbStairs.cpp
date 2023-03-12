// The climbing stairs is essentially the fibonacci sequence
// one step means you can add 1 to each of the one step ago.
// two step means you can add 2 to each of the two step ago.
// So total new steps -> all 1 steps ago + all 2 steps ago
// Quickest Solution
class Solution {
public:

    int climbStairs(int n) 
    {
        vector<int> ans(n+1, 0);

        // base cases
        
        if(n <= 0) return 0;
        if(n == 1) return 1;
        if(n == 2) return 2;
        
        ans[0] = 0;
        ans[1] = 1;
        ans[2] = 2;
        
        for(int i=3; i<=n; i++)
        {
            ans[i] = ans[i-1] + ans[i-2];
        }
        return ans[n];
    }
};

// Alternate Method
class Solution {
public:

    int climbStairs(int n) 
    {
        vector<int> ans;
        ans.push_back(0);
        ans.push_back(1);
        ans.push_back(2);
        for(int i = 3; i <= n; i++)
        {
            ans.push_back(ans[i-1] + ans[i-2]);
        }    
        return ans[n];
    }
};

// Slower due to one error in solution
class Solution {
public:

    vector<int> ans;
    
    int climbStairs(int n) 
    {
        ans.push_back(0);
        ans.push_back(1);
        ans.push_back(2);
        for(int i = 3; i <= n; i++)
        {
            ans.push_back(ans[i-1] + ans[i-2]);
        }    
        return ans[n];
    }
};