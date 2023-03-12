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
        if (left_pointer == right_pointer)  //If our left and right pointers overlap, then all possible swapping is finished
        {
            ans.push_back(nums);            //We can push back the current state of our nums array to our final answer
        }
        else 
        {
            for (int index = left_pointer; index <= right_pointer; index++)     //If indexes don't overlap
            {
                swap(nums[left_pointer], nums[index]);                          //Swap the left pointer with the index to get one permutation
                permute(nums, left_pointer + 1, right_pointer);                 //Recursively call the function with the next swap
                swap(nums[left_pointer], nums[index]);                          //Backtrack the swap that we have done
            
                //Here since we do the swapping first, we store the answer as we're undoing all the swappings. ie, we first find our result after the final swap
                //and then we keep appending them as we are also simultaneously undoing our swaps afterwards
            }
        }
    }
};