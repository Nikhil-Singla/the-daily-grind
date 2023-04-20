class Solution {
public:
    int numberOfSteps (int num) 
    {
            if(!num) return 0;
            int res = 0;
            while(num) 
            {
                res += (num & 1) ? 2 : 1;
                num >>= 1;
            }
            return res - 1;
    }
};

class Solution {
public:
    int numberOfSteps(int num) 
    {
        int ans = 0;
        while(num)
        {
            num = (num%2==0 ? num/2 : num-1);
            ans++;
        }    
        return ans;
    }
};

