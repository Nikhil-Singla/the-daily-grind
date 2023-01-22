class Solution {
public:
    int arrangeCoins(int n) 
    {
        int answer = 0;
        for(int i = 1; n > 0; i++)
        {
            if(n - i < 0)
            {
                break;
            }
            answer++;
            n -= i;
        }
        return answer;
    }
};