class Solution {
public:
    vector<vector<int>> groupThePeople(vector<int>& groupSizes) 
    {
        vector<vector<int>> solution;
        unordered_map<int, vector<int>> hash;
        for(int i = 0; i < groupSizes.size(); i++)
        {
            int assignment = groupSizes[i];
            if(hash[assignment].size() == assignment)
            {
                solution.push_back(hash[assignment]);
                hash[assignment].clear();
            }
            hash[assignment].push_back(i);
        }    
        for(auto &c : hash)
        {
            solution.push_back(c.second);
        }
        return solution;
    }
};