class Solution {
public:
    int findDuplicate(vector<int>& nums) 
    {
        unordered_map<int, int> map;
        for(int i=0; i<nums.size(); i++)
        {
            if(map[nums[i]] == nums[i])
            {return nums[i];}
            map[nums[i]] = nums[i];
        }
        return -1;    
    }
};