bool cmp(pair<int, int>& a, pair<int, int>& b)
{
    if(a.second < b.second)
    {
        return true;
    }
    else if((a.second == b.second) && a.first > b.first)
    {
        return true;
    }
    return false;
}

class Solution {
public:
    vector<int> frequencySort(vector<int>& nums) 
    {
        unordered_map<int, int> hash;
        vector<int> ans;
        for(int i = 0; i < nums.size(); i++)
        {
            hash[nums[i]]++;
        }
        vector<pair<int, int> > sorting_vector;
        for (auto& val : hash) 
        {
            sorting_vector.push_back(val);
        }
        sort(sorting_vector.begin(), sorting_vector.end(), cmp);
        for(pair<int, int>& val : sorting_vector)
        {
            while(val.second > 0)
            {
                ans.push_back(val.first);
                val.second--;
            }
        }
        return ans;
    }
};