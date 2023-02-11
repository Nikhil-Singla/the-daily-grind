class Solution {
public:
    int mostWordsFound(vector<string>& sentences) 
    {
        int ans = 0;
        for(auto i: sentences)
        {
            int temp = 1;
            for(auto c : i)
            {
                if(c == ' ') {temp++;}
            }
            ans = max(ans, temp);
        }
        return ans;
    }
};