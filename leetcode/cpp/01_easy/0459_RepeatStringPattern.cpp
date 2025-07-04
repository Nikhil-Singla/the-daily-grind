class Solution {
public:
    bool repeatedSubstringPattern(string s)
    {
        short lengthString = s.length();
        for(int i = 1; i <= lengthString/2; i++)
        {
            if(lengthString % i == 0)
            {
                string subString = s.substr(0, i);
                string repeatString = ""; 
                for(int j = 0; j < lengthString; j += i)
                {
                    repeatString += subString;
                }
                if(repeatString == s) {return true;}
            }
        }
        return false;
    }
};