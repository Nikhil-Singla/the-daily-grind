//Program to manually perform divison for 2 integers.
class Solution {
public:

    bool sign(int dividend, int divisor)        //Function to return the sign of the final answer based on 
    {                                           //divisor and dividend. True = answer is negative 
        bool negate = false;                    //Initialize
        if(dividend < 0)                        //If Dividend is negative
        {
            if(divisor < 0)                     //And divisor is also negative
            {}                                  //Negate stays false, ie result is positive
            else
            {negate = true;}                    //Otherwise result is negative
        }
        else                                    //If Dividend is positive
        {
            if(divisor >= 0)                    //And divisor is positive
            {}                                  //Negate stays false and result is positive
            else
            {negate = true;}                    //Otherwise result is negative
        }    
        return negate;                          //Return negate
    }

    int divide(int dividend, int divisor) 
    {
        bool negate = false;                    //Sign checker
        int result = 0;                         //Store answer here
        
        negate = sign(dividend, divisor);       //Get our initial signs
        
        if(dividend == INT_MIN)                 //Smallest number case because we cannot store it otherwise in absolute
        {                                       //function as we are converting everything to positive
            if(divisor > 0)
            {
                dividend += divisor;            //Division is nothing but taking away divisor from dividend
                result++;                       //Here dividend is negative(min) and hence we add the positive divisor
            }
            else
            {
                dividend -= divisor;            //And subtract the negative divisor 
                result++;
            }
        }

        dividend = abs(dividend);               //Convert to absolute values to make calc easier
        divisor = abs(divisor);

        for(; (dividend >= divisor) && (divisor!= 0); result++)     //Keep going till dividend is bigger than divisor as any less and we reach the remainder
        {                                                           //Make sure divisor isn't negative, and every time we take it away, we add 1 to the quotient
            if(result == INT_MAX)                                   //If we ever hit the max limit
            {
                return ( negate ? INT_MIN : INT_MAX );              //Check if we have negative, if we do, return Min possible value, otherwise Max possible
            }                                                       
            dividend -= divisor;                                    //Else we keep performing division by taking away divisor from dividend
        }    

        if(negate)                              //After exit loop, check if sign is negative during return
        {
            result *= -1;
        }

        return result;                          //Else return the correct answer
    }
};