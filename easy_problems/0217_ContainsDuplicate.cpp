class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_map<int, int>hash;
        if(nums.size()==1)
        {return false;}
        for(int i=0; i<nums.size(); i++)
        {
            if(hash[nums[i]] == 1)
            {
                return true;
            }
            hash[nums[i]] += 1;
        }
        return false;
    }
};
