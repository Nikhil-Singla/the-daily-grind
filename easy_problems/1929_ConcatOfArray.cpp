//Looked up the fastest solution and then wrote it myself with trial and error to understand the quickest way of solving questions.
class Solution {
public:
    vector<int> getConcatenation(vector<int>& nums) {
        int a = nums.size();
        for(int i = 0; i < a; i++)
        {
            nums.push_back(nums[i]);
        }
        return nums;
    }
};

//int size = nums.size() adds 3ms to the runtime
//Commenting itself also adds to the runtime, hence it has to be added post submission in github
//Theres some sort of weird bias for the variables used as using "n" gives a faster runtime than using "a". Except it might also be specific to the compiler and 
//website traffic that is actively using Leetcode. Not sufficient data.

//UNOPTIMIZED solution
/*class Solution {
public:
    vector<int> getConcatenation(vector<int>& nums) {
        vector<int> result;
        int size = nums.size();
        for(int i=0,j=0; i<(size*2);i++,j++)
        {
            if(j == size)
            {
                j = 0;
            }
            result.push_back(nums[j]);
        }
        return result;
    }
};
*/
