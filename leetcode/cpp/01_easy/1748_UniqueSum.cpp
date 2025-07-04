class Solution {
public:
    int sumOfUnique(vector<int>& nums) 
    {
        int ans = 0;
        unordered_map<int, int> hash;
        for(auto &c : nums)
        {
            hash[c]++; 
        }
        for(auto &c : hash)
        {
            if(c.second == 1)
            {
                ans += c.first;
            }
        }
        return ans;

    }
};