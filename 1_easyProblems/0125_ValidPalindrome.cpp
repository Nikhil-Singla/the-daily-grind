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

//CODE USING PURELY INBUILT FUNCTIONS
class Solution {
public:

    bool isPalindrome(string s) 
    {
        transform(s.begin(),s.end(),s.begin(), ::tolower);
        s.erase(remove_if(s.begin(),s.end(),[](char c){
            if((c >= 97 && c <= 122) || (c >= 48 && c <= 57))
                return false;
            return true;
        }), s.end());
        string t = s;
        reverse(t.begin(),t.end());
        return (t==s ? true : false);
    }
};