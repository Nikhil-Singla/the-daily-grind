class Solution {
public:
    vector<int> findErrorNums(vector<int>& nums) 
    {
        vector<int> ans;
        vector<bool> arr(nums.size()+1, false);
        int n = nums.size();
        for(uint const c : nums)
        {
            if(arr[c])
            {
                ans.push_back(c);
            }
            arr[c] = true;
        }
        for(uint i = 1; i < arr.size(); i++)
        {
            if(!arr[i])
            {
                ans.push_back(i);
                return ans;
            }
        }
        return {-1, -1};
    }
};

class Solution {
public:
    vector<int> findErrorNums(vector<int>& nums) 
    {
        vector<int> ans(2);
        int n = nums.size();
        int sum = (n*(n+1))/2;
        int numSum = 0;
        set<int> map;
        for(auto c : nums)
        {
            if(map.find(c) != map.end())
            {
                ans[0] = c;
            }
            numSum += c;
            map.insert(c);
        }
        ans[1] = sum - numSum + ans[0];
        return ans;
    }
};