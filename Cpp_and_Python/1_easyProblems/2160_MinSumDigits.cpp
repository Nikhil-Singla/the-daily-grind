// This is a class named Solution.
class Solution {
public:
    // This is a function named minimumSum that takes an integer as input and returns an integer.
    int minimumSum(int num) 
    {
        // This is a vector named digits that will store individual digits of the input number.
        vector<int> digits;
        // This is an integer named repetitions that is initially set to 4 and will be decremented in each iteration of the loop.
        int repetitions = 4;
        // This loop will run four times.
        while(repetitions--)
        {
            // This line gets the last digit of the input number and pushes it to the digits vector.
            digits.push_back(num%10);
            // This line removes the last digit of the input number.
            num /= 10;
        }    
        // This line sorts the digits vector in ascending order.
        sort(digits.begin(), digits.end());
        // This line calculates the minimum possible sum of two-digit numbers that can be formed from the digits vector and stores it in the sum variable.
        int sum = (digits[0]+digits[1])*10 + digits[2] + digits[3];
        // This line returns the sum variable as the output of the function.
        return(sum);
    }
};

