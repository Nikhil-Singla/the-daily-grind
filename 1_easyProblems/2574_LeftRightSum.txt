class Solution {
public:
    vector<int> leftRigthDifference(vector<int>& nums) 
    {
        if(nums.size() == 1)
        {
            return {0};
        }
        if(nums.size() == 2)
        {
            std::reverse(nums.begin(),nums.end());
            return nums; 
        }
        int leftSum = 0, rightSum = 0;
        vector<int> ans;
        int n = nums.size();
        for (auto n : nums)
        {
            rightSum += n;
        }
        for(auto n : nums)
        {
            rightSum -= n;
            ans.push_back(abs(leftSum - rightSum));
            leftSum += n;
        }
        return ans;
    }
};