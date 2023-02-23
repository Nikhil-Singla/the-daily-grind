class Solution {
public:
    int minimumOperations(vector<int>& nums) 
    {
        sort(nums.begin(), nums.end());
        int curr = 0;
        int operations = 0;
        for(auto c : nums)
        {
            if(c != curr)
            {
                curr = c;
                c = 0;
                operations++;
            }
            else
            {
                c = 0;
            }
        }
        return operations;
    }
};