// Slightly sophisticated code
class Solution {
public:
    int maxNumberOfBalloons(string text) 
    {
        int count[26] = {0};
        int res = INT_MAX;
        for(int i = 0; i < text.length(); i++)
        {
            count[text[i] - 'a']++;
        }
        string a = "ban";
        string b = "ol";
        for(auto &c : a)
        {
            res = min(res, count[c - 'a']);
        }
        for(auto &c : b)
        {
            res = min(res, count[c - 'a']/2);
        }
        return res;
    }
};

// Initial solution
class Solution {
public:
    int maxNumberOfBalloons(string text) 
    {
        int len[5] = {0};
        int count = 99999;
        for(int i = 0; i < text.length(); i++)
        {
            if(text[i] == 'b')
            {
                len[0]++;
            }
            if(text[i] == 'a')
            {
                len[1]++;
            }
            if(text[i] == 'n')
            {
                len[2]++;
            }
            if(text[i] == 'o')
            {
                len[3]++;
            }
            if(text[i] == 'l')
            {
                len[4]++;
            }
        }    
        for(int i = 0; i < 3; i++)
        {
            cout<<len[i]<<" ";
            count = min(count, len[i]);
        }
        for(int i = 3; i < 5; i++)
        {
            cout<<len[i]<<" ";
            count = min(count, len[i]/2);
        }
        return count;
    }
};