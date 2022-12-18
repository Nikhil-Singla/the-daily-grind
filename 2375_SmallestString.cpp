class Solution {
public:
    string smallestNumber(const string pattern) 
    {
        string result;
        char counter = '1';
        int dec = 0;
        bool flag;
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
            }
            flag = true;
            while(dec>0)
            {
                if(flag)
                {
                    i += dec;
                    flag = false;    
                }
                result += counter+dec;
                dec--;
            }
            cout<<result<<endl;
        }
        return result;
    }
};