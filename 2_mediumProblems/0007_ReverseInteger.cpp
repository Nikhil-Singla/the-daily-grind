class Solution {
public:
    int reverse(int x) 
    {
        unsigned int result = 0;
        if(x < 0)
        {
            if (x == INT_MIN)
            {
                return 0;
            }
            x *= -1;
            while(x != 0)
            {
                result = result*10 + x%10;
                x /= 10;
                if(result > INT_MAX)
                {

                }
            }

        }   
        else
        {

        } 
    }
};