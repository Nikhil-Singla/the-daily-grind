class Solution {
public:
    int arrangeCoins(int n) 
    {
        int l = 1; // l = lefr
        int r = n; // r = right

        while(l <= r)
        {
            long mid = l + (r - l ) / 2;
            if (n >= (mid * (mid + 1 ) /2 ))
            {
                l = mid + 1;
            }
            else
            {
                r = mid-1;
            }
        }
        return l-1;
    }
};

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