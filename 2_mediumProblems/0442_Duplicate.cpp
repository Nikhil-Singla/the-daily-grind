class Solution {
public:
    vector<int> findDuplicates(vector<int>& nums) 
    {
        vector<int> result;
        for(int i = 0; i<nums.size(); ++i)
        {
            int temp = abs(nums[i]) - 1;
            if(nums[temp] < 0)
            {
                result.push_back(temp+1);
                //cout<<temp<<" ";
            } 
            nums[temp] *= -1;
        }     
        return result;
    }
};