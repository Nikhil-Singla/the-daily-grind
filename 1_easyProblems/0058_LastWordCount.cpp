class Solution {
public:
    int lengthOfLastWord(string s) 
    {
        int count = 0;
        int last = 0;
        for(auto c: s)
        {
            if(c == ' ')
            {
                if(count == 0)
                {}
                else
                {
                    last = count;
                    count = 0;
                }
            }
            else
            {
                count++;
                last = -1;
            }
        }    
        return max(count, last);
    }
};