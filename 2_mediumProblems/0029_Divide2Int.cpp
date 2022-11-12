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
        bool negate = false;
        int result = 0;
        
        negate = sign(dividend, divisor);
        
        if(dividend == INT_MIN)
        {
            if(divisor > 0)
            {
                dividend += divisor;
                result++;
            }
            else
            {
                dividend -= divisor;
                result++;
            }
        }
        dividend = abs(dividend);
        divisor = abs(divisor);

        for(; (dividend >= divisor) && (divisor!= 0); result++)
        {
            if(result == INT_MAX)
            {return (negate?INT_MIN:INT_MAX);}
            dividend -= divisor;
        }    

        if(negate)
        {
            result *= -1;
        }

        return result;
    }
};