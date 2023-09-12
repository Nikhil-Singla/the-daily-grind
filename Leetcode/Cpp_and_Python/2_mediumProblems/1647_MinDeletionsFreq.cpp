class Solution {
public:
    int minDeletions(string s) 
    {
        vector<int> alphabet(27, 0); 
        for(auto &c : s)
        {
            alphabet[c - 'a']++;
        }   
        unordered_set<int> used_freq;
        uint result = 0;
        for(auto &c : alphabet)
        {
            while((c > 0) && used_freq.find(c) != used_freq.end())
            {
                c--;
                result++;             
            }
            used_freq.insert(c);
        }        
        return result;
    }
};