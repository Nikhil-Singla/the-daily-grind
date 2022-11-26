class Solution {
public:

    vector<vector<int>> ans;

    vector<vector<int>> permuteUnique(vector<int>& nums) 
    {
        if(nums.size()==1)
        {
            ans.push_back(nums);
            return ans;
        }
        sort(nums.begin(), nums.end());
        permute(nums, 0, nums.size()-1);

        return ans;

    }

    void permute(vector<int>& nums, int left_pointer, int right_pointer)
    {
        if (left_pointer == right_pointer)
        {
            bool flag = true;
            for(int j = 0; j < ans.size(); j++)
            {
                if(ans[j] == nums)
                {
                    flag = false;
                }
            }
            if(flag)
            {
                ans.push_back(nums);
            }
        }
        else 
        {
            for (int index = left_pointer; index <= right_pointer; index++) 
            {
                swap(nums[left_pointer], nums[index]);
                permute(nums, left_pointer + 1, right_pointer);
                swap(nums[left_pointer], nums[index]);
            }
        }
    }
};