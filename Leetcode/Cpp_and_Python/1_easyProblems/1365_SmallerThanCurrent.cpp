class Solution {
public:
    vector<int> smallerNumbersThanCurrent(vector<int>& nums) 
    {
        int count[101] = {0};
        for(auto const c : nums)
        {
            count[c] += 1;
        }
        int res[101] = {0};
        res[0] = 0;
        for(int i = 1; i < 101; i++)
        {
            res[i] = count[i-1] + res[i-1];
        }
        for(int i = 0; i < nums.size(); i++)
        {
            nums[i] = res[nums[i]];
        }
        return nums;
    }
};