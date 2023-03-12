class Solution {
public:

    bool buddyStrings(string s, string goal) 
    {
        if(s.length() != goal.length())
        {return false;}
        int alphabets[26] = {0};
        bool flag = false;
        int count = 0;
        vector<pair<char, char>> difference;
        for(uint i = 0; i < s.length(); i++)
        {
            if(s[i] != goal[i])
            {
                count++;
                if(count > 2) {return false;}
                pair<char, char> temp(s[i], goal[i]);
                difference.push_back(temp);
            }
            else if(!flag)
            {
                alphabets[s[i] - 'a']++;
                if(alphabets[s[i] - 'a'] >= 2) {flag = true;}
            }
        }
        return ((count == 2 && (difference[0].first == difference[1].second) && (difference[1].first == difference[0].second)) || (!count && flag));
    }
};