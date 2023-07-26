// This is a class named "Solution" that contains a function named "threeConsecutiveOdds"
class Solution {
public:
    // The function takes in a vector of integers called "arr" which is the problem array and returns a boolean value
    bool threeConsecutiveOdds(vector<int>& arr) 
    {
        // Initialize a variable "count" to keep track of the number of consecutive odd integers found
        int count = 0;
        // Iterate through each element of the vector using a for loop
        for(int i = 0; i < arr.size(); i++)
        {
            // Check if the current element is odd by using the modulus operator
            if(arr[i] % 2 == 1)
            {
                // If the current element is odd, increment the count of consecutive odd integers found
                count++;
            }
            else
            {
                // If the current element is even, reset the count to 0
                count = 0;
            }
            // Check if there are 3 consecutive odd integers found
            if(count == 3)
            {
                // If there are 3 consecutive odd integers found, return true
                return true;
            }
        }
        // If there are no 3 consecutive odd integers found, return false
        return false;
    }
};
