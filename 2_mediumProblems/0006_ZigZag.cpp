class Solution {
public:
    string convert(string s, int numRows) 
    {
        if(numRows == 1)
        {
            return s;
        }

        int skipper = (numRows-1) * 2; // How many elements we skip per letter
        int evenSkipper = numRows/2;
        int index = 0;
        int loopNum = 1;
        int len = s.size();
        string result;

        for(int counter = 0; counter < len; counter++)
        {
            if(index > len-1)
            {
                index = loopNum++;
            }
            result.push_back(s[index]);
            if(loopNum%2 == 1)
            {
                index += skipper;
            }
            else
            {
                index += evenSkipper;
            }
        }
        return result;
    }
};