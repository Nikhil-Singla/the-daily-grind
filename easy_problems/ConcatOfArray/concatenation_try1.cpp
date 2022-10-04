class Solution {
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
