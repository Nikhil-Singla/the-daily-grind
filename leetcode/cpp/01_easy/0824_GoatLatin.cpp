class Solution {
public:

    bool isVowel(char a)
    {
        a = tolower(a);
        return (a == 'a' || a =='e' || a == 'i' || a == 'o' || a=='u');
    }

    string numberOfA(int length)
    {
        return std::string(length, 'a');
    }

    string toGoatLatin(string sentence) 
    {
        string word = "";
        vector<string> result;
        for(auto c : sentence)
        {
            if (c == ' ')
            {
                result.push_back(word);
                word = "";
            }
            else 
            {
                word = word + c;
            }
        }   
        result.push_back(word);
        int counter = 1;
        string ans="";
        for(auto c : result)
        {
            if(isVowel(c[0]))
            {}
            else
            {
                c += c[0];
                c.erase(c.begin());
            }
            c += "ma";
            c += numberOfA(counter++);
            ans += c + " ";
        } 
        ans.pop_back();
        return ans;
    }
};