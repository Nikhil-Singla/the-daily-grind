class Solution {
public:
    int longestPalindrome(string s) 
    {
        if(s.length() < 2)
        {return 1;}

        unordered_map <char, int> map;
        for(auto c : s)
        {
            map[c]++;
        }

        int ans = 0;
        bool flag = false;
        for(auto c : map)
        {
            ans += (c.second/2)*2;
            if(c.second%2 == 1)
            {
                flag = true;
            }
        }
        return ans+flag;
    }
};