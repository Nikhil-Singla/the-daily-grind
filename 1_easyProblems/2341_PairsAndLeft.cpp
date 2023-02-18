class Solution {
public:
    vector<int> numberOfPairs(vector<int>& nums) 
    {
        unordered_map<int, int> address;
        vector<int> res(2);
        res[0] = 0;
        res[1] = 0;
        while(nums.size())
        {
            if(address[nums.back()] > 0)
            {
                res[0]++;
                address[nums.back()] = -1;
                nums.pop_back();
            }
            else
            {
                address[nums.back()] = 1;
                nums.pop_back();
            }
        } 
        for(auto c : address)
        {
            if(c.second > 0)
            res[1]++;
        }
        return res;
    }
};