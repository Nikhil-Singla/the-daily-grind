class Solution {
public:
    int majorityElement(vector<int>& nums) {
        unordered_map<int, int> hash;
        int majority = nums.size()/2;
        for(int i = 0; i<nums.size(); i++)
        {
            hash[nums[i]] += 1;
            if(hash[nums[i]] > majority)
            {
                return nums[i];
            }
        }
        return 0;
    }
};

// ALTERNATE SOLUTION using inbuilt sorting

class Solution {
public:
    int majorityElement(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        return nums[nums.size()/2];
    }
};