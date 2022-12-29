class Solution {
public:
    int findMiddleIndex(vector<int>& nums) 
    {
        int leftSum = 0, rightSum = 0, mid = 0;
        for(int i = 1; i < nums.size(); i++)
        {
            rightSum += nums[i];
        }    
        for(int i = 0; i < nums.size(); i++)
        {
            if(leftSum == rightSum)
            {
                return i;
            }
            leftSum += nums[i];
            (i+1 == nums.size()) ? rightSum = 0 : rightSum -= nums[i+1];
        }
        return -1;
    }
};