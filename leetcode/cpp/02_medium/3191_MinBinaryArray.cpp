class Solution {
public:
    int minOperations(vector<int>& nums) 
    {
        uint count = 0, i;
        for(i = 0; i < nums.size()-2; i++)
        {
            if (!nums[i])
            {
                count++;
                nums[i+1] ^= 1;
                nums[i+2] ^= 1;
            
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
