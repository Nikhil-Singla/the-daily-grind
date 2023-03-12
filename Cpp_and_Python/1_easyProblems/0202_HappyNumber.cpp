class Solution {
public:

    uint sumSquares(uint j)
    {
        uint result = 0;
        while(j)
        {
            result += (j%10)*(j%10);
            j /= 10;
        }
        return result;
    }

    bool isHappy(uint n) 
    {
        unordered_map<uint, bool> hash;
        hash[n] = true;
        while(n != 1)
        {
            n = sumSquares(n);
            if(hash[n])
            {
                return false;
            }
            hash[n] = true;
        }
        return true;
    }
};