class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) 
    {
        unordered_map<int, int> hash;
        vector<int> ans;
        for(int i = 0; i < nums1.size(); i++)
        {
            hash[nums1[i]]++;
        }    
        for(int i = 0; i < nums2.size(); i++)
        {
            if(hash[nums2[i]] > 0)
            {
                ans.push_back(nums2[i]);
            }
        }
        set<int> unique( ans.begin(), ans.end() );
        ans.assign( unique.begin(), unique.end() );
        return ans;
    }
};

class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) 
    {
        unordered_map<int, int> hash;
        vector<int> ans;
        unordered_set<int> unique;
        for(int i = 0; i < nums1.size(); i++)
        {
            hash[nums1[i]]++;
        }    
        for(int i = 0; i < nums2.size(); i++)
        {
            if(hash[nums2[i]] > 0)
            {
                unique.insert(nums2[i]);
            }
        }
        ans.assign( unique.begin(), unique.end() );
        return ans;
    }
};