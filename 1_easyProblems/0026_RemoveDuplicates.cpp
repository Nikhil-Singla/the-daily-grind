

// Copied solution to study further
int removeDuplicates(vector<int>& nums) {
    int i = 0;
    for (int n : nums)
        if (!i || n > nums[i-1])
            nums[i++] = n;
    return i;
}


// BRUTE FORCE SOLUTION
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