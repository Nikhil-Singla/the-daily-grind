class Solution {
public:
    int first, second;
    bool containsNearbyDuplicate(vector<int>& nums, int k) 
    {
        unordered_map<int, int>hash;
        if(nums.size()==1||k==0)
        {return false;}
        for(int i=0; i<nums.size(); i++)
        {
            if(hash.count(nums[i]))
            {
                int val = abs(hash[nums[i]]-i);
                if(val<=k)
                {return true;}
            }
            hash[nums[i]] = i;
        }
        return false;
    }
};
