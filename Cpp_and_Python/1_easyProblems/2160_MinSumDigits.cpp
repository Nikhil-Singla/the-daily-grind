class Solution {
public:
    int minimumSum(int num) 
    {
        vector<int> digits;
        int repetitions = 4;
        while(repetitions--)
        {
            digits.push_back(num%10);
            num /= 10;
        }    
        sort(digits.begin(), digits.end());
        int sum = (digits[0]+digits[1])*10 + digits[2] + digits[3];
        return(sum);
    }
};