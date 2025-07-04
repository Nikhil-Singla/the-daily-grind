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


#include <stdlib.h>
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<pair<int, int>> pairs; //Declare vector of datatype "pair" and both elements of the pair/tuple being int
        for(int i=0; i<nums.size();i++)
        {
            pairs.push_back({nums[i],i}); //Push the elements of the original vector to the pair vector
        }
        sort(pairs.begin(), pairs.end()); //Sort the pair's vector to arrange
        int left = 0, right = nums.size()-1; //Assign two "markers". Left and Right
        while(left<right)
        {
            if(pairs[left].first + pairs[right].first == target) //If statement to match target. First refers to the first number of the pair.
            {
                return {pairs[left].second, pairs[right].second}; //Return the second number of the pair which is the index of the element from the original vector
            }
            if(pairs[left].first + pairs[right].first < target) //If the sum is below target, we need to increase min value by going right from the lowest (left) marker
            {
                left++;
            }
            if(pairs[left].first + pairs[right].first > target) //If the sum is above target, we need to dec. max value by going left from the highest (right) marker
            {
                right--;
            }
        }
        return {}; //Return null if no solution
    }
};
