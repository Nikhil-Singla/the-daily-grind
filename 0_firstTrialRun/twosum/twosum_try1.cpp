#include <stdlib.h>
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        for(int i = 0; i<nums.size()-1; i++) //First run through the entire array with the i'th element starting from 0 
        {
            for(int j = i+1; j<nums.size();j++) //At the same time, run with the j'th element which is starting from i+1
            {
                if((nums[i]+nums[j])==target) //If the sum of i'th and the j'th element is target, then output
                {
                    return{i, j}; //Return as vector
                }
            }
        }
        return {}; //Return null if no solution
    }
};
