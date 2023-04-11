class Solution {
public:
    int smallestEqual(vector<int>& nums) 
    {
        // Loop through each number in the vector
        for(int i = 0, count = 0; i < nums.size(); i++, count++)
        {
            // If count reaches 10, reset it to 0
            if(count == 10)
            {
                count = 0;
            }
            // If the current number is equal to count, return its index
            if(nums[i] == count)
            {
                return i;
            }
        }
        // If no number is equal to its index, return -1
        return -1;
    }
};
