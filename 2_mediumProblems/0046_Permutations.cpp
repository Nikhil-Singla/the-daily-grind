class Solution {
public:

    vector<vector<int>> ans;                // Variable to store answer

    vector<vector<int>> permute(vector<int>& nums) 
    {
        if(nums.size()==1)                  //If we only have one element
        {
            ans.push_back(nums);            //Just push back the element vector to our answer
            return ans;                     //and return the answer
        }

        permute(nums, 0, nums.size()-1);    //Call permute function to get the answer from nums array using its first and last indexes to call the function
        return ans;                         //Permute function modifies answer

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