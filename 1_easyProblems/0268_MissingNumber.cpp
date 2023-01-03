class Solution {
public:
    int missingNumber(vector<int>& nums) 
    {
        unordered_map<int, bool> hash;
        for(auto& c : nums)
        {
            hash[c] = true;
        }    
        for(int i = 0; i <= nums.size(); i++)
        {
            if(hash[i])
            {}
            else
            {
                return i;
            }
        }
        return 1;
    }
};