class Solution {
public:
    vector<string> findRestaurant(vector<string>& list1, vector<string>& list2) 
    {
        vector<string> output;
        int min = INT_MAX;
        int counter = 0;
        unordered_map<string, int> map;
        for(auto c : list1)
        {
            if(map.find(c) == map.end())
            {
                map[c] = counter;
            }
            counter++;
        }

        for(int i = 0; i < list2.size(); i++)
        {
            if(map.find(list2[i]) == map.end())
            {}
            else
            {
                if( min == i + map[list2[i]] )
                {
                    output.push_back(list2[i]);
                }
                if( min > i + map[list2[i]] )
                {
                    min = i + map[list2[i]];
                    while(!output.empty())
                    {
                        output.pop_back();
                    }
                    output.push_back(list2[i]);
                }

            }
        }
        return output;
    }
};