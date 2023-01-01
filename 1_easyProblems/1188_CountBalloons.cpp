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