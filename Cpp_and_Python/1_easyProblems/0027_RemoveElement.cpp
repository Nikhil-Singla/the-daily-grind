/**
The removeElement function takes a vector of integers nums and an integer val, and removes 
all instances of val from the vector. The function returns the length of the modified vector.
**/

class Solution {
public:
    int removeElement(vector<int>& nums, int val) 
    {
        // Initialize a variable to keep track of the next available index in the modified vector
        uint nextIndex = 0;

        // Iterate over each element of the input vector
        for(uint i = 0; i < nums.size(); i++)
        {
            // If the current element is not equal to the value to be removed, copy it to the next available index
            if(nums[i] != val) 
            {
                nums[nextIndex++] = nums[i];
            }
            // If the current element is equal to the value to be removed, do nothing
            else
            {}
        }

        // Return the index of the last element in the modified vector
        return nextIndex;
    }
};