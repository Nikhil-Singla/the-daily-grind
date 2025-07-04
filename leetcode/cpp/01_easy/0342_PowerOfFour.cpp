// Uploaded an explanation of this solution on LeetCode.
class Solution {
public:
    bool isPowerOfFour(int x) 
    {
        if(x < 1)
        {
            return false;
        }
        if(x == 1)
        {
            return true;
        }
        return (ceil(log2(x)/2) == floor(log2(x)/2));
    }
};

class Solution {
public:
    bool isPowerOfFour(int n) 
    {
        if(n < 1)
        {
            return false;
        }    
        while(n > 1)
        {
            if(n%4 != 0)
            {
                return false;
            }
            n /= 4;
        }
        return true;
    }
};