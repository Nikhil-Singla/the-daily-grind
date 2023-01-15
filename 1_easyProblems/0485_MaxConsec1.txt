class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) 
    {
        uint count = 0;
        uint ans = 0;
        for(short const c : nums)
        {
            if(c & 1) {count++;}
            else {
                ans = max(ans, count);
                count = 0;
            }
        }    
        ans = max(ans, count);
        return ans;
    }
};