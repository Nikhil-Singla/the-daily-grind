class Solution {
public:
    bool areNumbersAscending(string s) {
        int max = -1;
        string currNum;
        s.push_back(' ');
        for(int i = 0 ; i < s.size() ; i++)
        {
            char ch = s[i];
            if(isdigit(ch)) {currNum += ch;}
            else if(ch == ' ' && isdigit(s[i - 1]))
            {
                if(stoi(currNum) <= max) {return false;}
                max = stoi(currNum);
                currNum = "";
            }
        }
        return true;
    }
};
