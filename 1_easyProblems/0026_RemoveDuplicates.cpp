class Solution {
public:
    int removeDuplicates(vector<int>& nums) 
    {
        auto pointer = nums.begin()+1;
        for(int i = 1; i < nums.size(); i++, pointer++)
        {
            if(nums[i] == nums[i-1])
            {
                i--;
                pointer--;
                nums.erase(pointer);
            }
        }

        return nums.size();
    }
};