#include <stdlib.h>
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<pair<int, int>> pairs;
        for(int i=0; i<nums.size();i++)
        {
            pairs.push_back({nums[i],i});
        }
        sort(pairs.begin(), pairs.end());
        int left = 0, right = nums.size()-1;
        while(left<right)
        {
            if(pairs[left].first + pairs[right].first == target)
            {
                return {pairs[left].second, pairs[right].second};
            }
            if(pairs[left].first + pairs[right].first < target)
            {
                left++;
            }
            if(pairs[left].first + pairs[right].first > target)
            {
                right--;
            }
        }
        return {};
    }
};
