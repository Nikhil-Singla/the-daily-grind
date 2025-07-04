class Solution {
public:
    int minOperations(vector<int>& nums, int x) 
    {
        int target = 0, n = nums.size();
        for( int number : nums) target += number;
        target -= x;

        if(target == 0) return n;

        int maxLength = 0, currentSum = 0, left = 0;

        for(int right = 0 ; right < n ; right++)
        {
            currentSum += nums[right];
            while(left <= right && currentSum > target)
            {
                currentSum -= nums[left++];
            }
            if(currentSum == target)
            {
                maxLength = max(maxLength, right-left+1);
            }
        }
        return maxLength ? n - maxLength : -1;
    }
};