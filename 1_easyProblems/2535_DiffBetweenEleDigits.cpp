class Solution {
public:
    
    int sumDigits(int number)
    {
        int sum = 0;
        while(number){
            sum += number%10;
            number /= 10;
        }
        return sum;
    }
    
    int differenceOfSum(vector<int>& nums) 
    {
        int res = 0;
        for(int const c : nums){
            res += c - sumDigits(c);
        }
        return abs(res);
    }
};