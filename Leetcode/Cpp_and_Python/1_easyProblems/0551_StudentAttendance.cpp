class Solution {
public:
    bool checkRecord(string s) 
    {
        uint alreadyAbsent = 0;
        uint lateCount = 0;
        for(auto c : s)
        {   
            if(c == 'A')
            {
                lateCount = 0;
                if(alreadyAbsent) {return false;}
                else {alreadyAbsent++;}
            }
            else if(c == 'L') 
            {
                lateCount++;
                if(lateCount == 3) {return false;}
            }
            else {lateCount = 0;}
        }
        return true;
    }
};