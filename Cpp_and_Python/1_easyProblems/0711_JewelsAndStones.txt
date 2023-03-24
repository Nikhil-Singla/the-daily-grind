class Solution {
public:
    int numJewelsInStones(string jewels, string stones) 
    {
        unordered_set<char> finder;
        for(auto c : jewels)
        {
            finder.insert(c);
        }    
        int count = 0;
        for(auto c : stones)
        {
            if(finder.find(key) != finder.end())
            {
                count++;
            }
        }
        return count;
    }
};