class Solution {
public:

    vector<vector<int>> ans;

    vector<vector<int>> permute(vector<int>& nums) 
    {
        if(nums.size()==1)
        {
            ans.push_back(nums);
            return ans;
        }

        permute(nums, 0, nums.size()-1);
        return ans;

    }

    void permute(vector<int>& nums, int left_pointer, int right_pointer)
    {
        if (left_pointer == right_pointer)
        {
            ans.push_back(nums);
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