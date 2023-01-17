class Solution {
public:
    int findPoisonedDuration(vector<int>& tS, int duration) 
    {
        int seconds = 0;
        for(int i = 0 ; i < tS.size()-1; i++)
        {
            if(tS[i] + duration > tS[i+1])
            {
                seconds += tS[i+1] - tS[i];
            }
            else
            {
                seconds += duration;
            }
        }
        return seconds+duration;
    }
};