class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int xor1=nums[0];
        for(int i=0;i<nums.size();i++){
            xor1=xor1^nums[i];
        }
        return xor1;
    }
};

class Solution {
public:
    int singleNumber(vector<int>& nums) 
    {
        unordered_map<int, int>hash;
        for(int i = 0; i<nums.size();i++)
        {
            if(hash[nums[i]]==1)
            {
                hash[nums[i]] = -1;
            }
            hash[nums[i]]++; 
        }
        for(int i = 0; i<nums.size();i++)
        {
            if(hash[nums[i]]==1)
            {
                return nums[i];
            }
        }
        return nums[0];

    }
};
