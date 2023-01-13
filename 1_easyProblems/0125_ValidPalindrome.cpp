#include <cctype>
class Solution {
public:
    bool isvalid(char ch)
    {
        if((ch>='A'&& ch<='Z')|| (ch>='a'&& ch<='z')|| (ch>='0'&& ch<='9')){
            return true;
        }
        return false;
    }
    bool isPalindrome(string s) 
    {
        string phrase;
        for(auto c : s)
        {
            if(isvalid(tolower(c)))
            {
                phrase += tolower(c);
            }
        }
        int start = 0, end = phrase.length()-1;
        while(start < end)
        {
            if(phrase[start++] != phrase[end--])
            {
                return false;
            }
        }
        return true;
    }
};
