class Solution {
public:

    bool sign(int dividend, int divisor)
    {
        bool negate = false;
        if(dividend < 0)
        {
            if(divisor < 0)
            {}
            else
            {negate = true;}
        }
        else
        {
            if(divisor >= 0)
            {}
            else
            {negate = true;}
        }    
        return negate;
    }

    int divide(int dividend, int divisor) 
    {
        bool sign = sign(dividend, divisor);
        
    }
};