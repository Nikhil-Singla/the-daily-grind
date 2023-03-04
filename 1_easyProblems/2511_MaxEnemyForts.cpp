class Solution {
public:
    int captureForts(vector<int>& forts) 
    {
        int result = 0;
        vector<int> empty, ally;
        for(int i = 0; i < forts.size(); i++)
        {   
            if(forts[i] == -1) {empty.push_back(i+1);}
            if(forts[i] == 1) {ally.push_back(i+1);}
        }    
        int prev = 1100;
        for(auto c : ally)
        {
            for(auto d : empty)
            {
                if(prev < 1001) {;} 
                if(d < c) {result = max(result, c - d - 1);}
                else if(d > c) {result = max(result, d - c - 1);}
            }
            prev = c;
        }
        return result;
    }
};