class Solution {
public:
    int distributeCandies(vector<int>& candyType) 
    {
        set<int> s(candyType.begin(), candyType.end());
        return min(candyType.size()/2, s.size());
    }
};

class Solution {
public:
    int distributeCandies(vector<int>& candyType) 
    {
        int typesOfCandy = 0;
        unordered_map <int, bool> map;
        for(auto c : candyType)
        {
            if(map[c])
            {}
            else
            {
                map[c] = true;
                typesOfCandy += 1;
                if(typesOfCandy >= candyType.size()/2)
                {break;}
            }
        }
        return typesOfCandy;
    }
};