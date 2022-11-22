class Solution {
public:

    int reverse(int x) 
    {
        if(x == INT_MIN)                            // Min length number, auto reverse to zero 
        {
            return 0;
        }
        
        if(x < 0) 
        {
            return (reverse(-x)*-1);                //If x is negative, call it with a positive and add negative at the end, during return.
        }

        int result = 0;                             //Initialize return to 0
        
        while(x > 0)                                //Exit condition otherwise we keep reversing digit by digit
        {
            int a = x % 10;                         //Get the units digit from x
            x = x / 10;                             //Change the value of x
            if( (INT_MAX - a)/10 < result )         //To prevent overflow, we check if the digit can be subtracted and divided by 10 from Max Possible. If not, then it returns 0
            {   
                return 0;                           //Return 0 if overflow
            }
            result = result * 10 + a;               //Add the units digit to the result which is reversing
        }
        return result;                              //Return the correct result
    }

};