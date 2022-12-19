class Solution {
public:
    vector<int> getSumAbsoluteDifferences(const vector<int> nums) 
    {
        vector<int> result;
        result.push_back(0);
        int n = nums.size();
        for(int i = 1; i<n; i++)
        {
            result[0] += nums[i] - nums[0];
        }    
        for(int i = 1; i < n; i++)
        {
            int diff = nums[i] - nums[i-1];
            int add = (i)*diff;
            int sub = (n-i)*diff;
            result.push_back(result[i-1] + add - sub);
        }
        return result;
    }
};