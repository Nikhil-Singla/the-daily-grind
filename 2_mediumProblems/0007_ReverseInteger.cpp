class Solution {
public:

    int reverse(int x) 
    {
        if(x == INT_MIN) 
        {
            return 0;
        }
        
        if(x < 0) 
        {
            return (reverse(-x)*-1);
        }

        int result = 0;
        
        while(x > 0)
        {
            int a = x % 10;
            x = x / 10;
            if( (INT_MAX - a)/10 < result ) 
            {
                return 0;
            }
            result = result * 10 + a;
        }
        return result;
    }

};