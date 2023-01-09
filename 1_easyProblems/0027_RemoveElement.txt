class Solution {
public:
    int removeElement(vector<int>& nums, int val) 
    {
        uint nextIndex = 0;
        for(uint i = 0; i < nums.size(); i++)
        {
            if(nums[i] == val)
            {}
            else
            {
                nums[nextIndex++] = nums[i];
            }
        }
        return nextIndex;
    }
};