class Solution {
public:
    int distinctIntegers(int n) 
    {
        if(n==1)
        {return n;}
        return n-1; 
    }
};

// Due to huge number of days, n-1 leaves a % remainder of 1, so all numbers will be on the board one by one,
// due to n being less than 100 except for 1, unless it is 1 itself 