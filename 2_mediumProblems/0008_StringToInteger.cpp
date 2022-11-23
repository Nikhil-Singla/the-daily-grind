class Solution {
public:
    bool isNum(char a)          //Function to check if the input char is a number or not
    {
        if(a < 58 && a>47)      //ASCII code based checker
        {
            return true;        //Character is number
        }
        return false;           //Character is not number
    }

    int myAtoi(string s)        //Convert string to int
    {
        long long result = 0;   //Store our result
        int i = 0;              //Keep track of the current input character from the entire string
        bool negate = false;    //Keep track if the number is negative or not

        while(s[i] == ' ')      //If the string has spaces in the beginning, keep moving the index pointer forward
        {
            i++;
        }
        if(s[i] == '-')         //If we find the negative sign, the final answer has to be negative.
        {
            negate = true;
            i++;
        }
        else if(s[i] == '+')    //If we find the positive sign, ignore it
        {
            i++;
        }
        while(isNum(s[i]))      //If the index after is a number
        {
            result = result*10 + (s[i] - 48);   //Add the index to result
            i++;
            if(result >= INT_MAX)               //If result exceeds the max value, we can stop as any further
            {                                   //Further digits will only make the answer larger and we need 
                break;                          //to clamp the result
            }   
        }

        if(negate)                              //Check if the answer is supposed to be negative or not
        {
            result *= -1;
        }
        if(result <= INT_MIN)                   //Clamp from the lower side
        {
            return INT_MIN;
        }
        if(result >= INT_MAX)                   //Clamp from the upper side
        {
            return INT_MAX;
        }

        return result;                          //If not clamping, our result remains unchanged
    }
};
