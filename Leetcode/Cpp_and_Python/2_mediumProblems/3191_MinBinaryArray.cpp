class Solution {
public:
    int minOperations(vector<int>& nums) 
    {
        uint count = 0, i;
        uint length = nums.size()-2;
        for(i = 0; i < nums.size()-2; i++)
        {
            if (nums[i] == 0)
            {
                count++;
                nums[i] = 1;
                nums[i+1] = (nums[i+1] ? 0 : 1);
                nums[i+2] = (nums[i+2] ? 0 : 1);
            
            }
        }
        if(nums[i] && nums[i+1])
        {
            return count;
        }
        else
        {
            return -1;
        }

    }
};