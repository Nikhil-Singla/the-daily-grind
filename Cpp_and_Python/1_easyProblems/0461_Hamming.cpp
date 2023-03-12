class Solution {
public:
    int hammingDistance(int x, int y) 
    {
        int b = x ^ y;
        int c = 0;
        while(b)
        {
            c += b & 1;
            b >>= 1;
        }
        return c;
    }
};