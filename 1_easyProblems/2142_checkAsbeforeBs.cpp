class Solution {
public:
    bool checkString(string s) {
        bool condition = false;
        for(int i = 0; i<s.size(); i++)
        {
            if(s[i] == 'b')
            {
                condition = true;
            }
            if(condition)
            {
                if(s[i] == 'a')
                {
                    return false;
                }
            }
        }
        return true;
    }
};

// ALTERNATE SOLUTION

bool checkString(string s) {
        return s.find("ba")==string::npos;
    }
// If at any point, a comes after b, ba would appear in the string.

