class Solution {
public:
    int alternateDigitSum(int n) 
    {
        int sum = 0;
        int alt = 1;
        vector<int> digits;
        while(n)
        {
            digits.push_back(n%10);
            n /= 10;
        }
        std:reverse(digits.begin(), digits.end());
        for(auto c : digits)
        {
            sum += (c)*(alt);
            alt *= -1;
        }    
        return sum;
    }
};