class Solution {
public:
    string smallestNumber(const string pattern) 
    {
        string result;
        char counter = '1';
        int dec = 0;
        for(int i = 0; i < pattern.length(); i++)
        {
            if(pattern[i] == 'I')
            {
                result += counter;
                counter++;
            }
            while(pattern[i] == 'D')
            {
                dec++;
                i++;
            }
            while(dec>0)
            {
                result += counter+dec;
                dec--;
            }
        }
        result += counter;
        return result;
    }
};