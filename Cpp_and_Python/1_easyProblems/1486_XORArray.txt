class Solution {
public:
    int xorOperation(int n, int start) 
    {
        int index = 0;
        int ans = 0;
        while(n--)        
        {
            int temp;
            temp = start+2*index++;
            ans ^= temp;
        }    
        return ans;
    }
};