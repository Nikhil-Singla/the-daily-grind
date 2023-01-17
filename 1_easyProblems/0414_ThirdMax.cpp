class Solution {
public:
    int thirdMax(vector<int>& nums) 
    {
        set<int> ans(nums.begin(), nums.end());
        auto ret = ans.rbegin();
        if(ans.size() < 3)
        {return *(ret);}
        else
        {return *(++++ret);} 
    }
};