class Solution {
public:
    string decodeMessage(string key, string message) 
    {
        int characters[26] = {0};
        vector<char> converted(26);
        int index = 0;
        for(auto c : key)
        {
            if(c == ' ')
            {}
            else if(characters[c - 'a'])
            {}
            else
            {
                characters[c-'a']++;
                converted[index] = c;
                index++;
            }
        }
        string ans = "";
        //for(auto c : converted)
        //{
        //    cout<<c;
        //}
        for(auto c : message)
        {
            if(c == ' ')
            {
                ans += ' ';
            }
            else
            {
                vector<char>::iterator letter = find(converted.begin(), converted.end(), c);
                //cout<<*(letter);
                int index = letter - converted.begin();
                char charac = index + 97;
                ans += charac;
            } 
        }
        return ans;
    }
};