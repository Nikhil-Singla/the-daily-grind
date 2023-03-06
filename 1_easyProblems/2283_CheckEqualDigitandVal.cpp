class Solution {
public:
    bool digitCount(string nums) 
    {
        unordered_map<int, int> hash;
        unordered_map<int, int> occurence;
        int i = 0;
        for(auto c : nums)
        {
            int a = c - '0';
            hash[i] = a;
            occurence[a]++;
            i++;
        }    

        for(auto c : hash)
        {
            if(occurence[c.first] != c.second)
            {
                return false;
            }
        }
        return true;
    }
};