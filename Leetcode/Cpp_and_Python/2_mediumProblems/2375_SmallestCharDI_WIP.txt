class Solution {
public:
    string smallestNumber(const string pattern) 
    {
        string result;
        int i = 0;
        int n = pattern.length() + 49;
        char front_stream = '1';
        char back_stream = n;
        while(front_stream <= back_stream)
        {
            if(pattern[i++] == 'I') result += front_stream++;
            else result += back_stream--;
        }
        return result;
    }
};