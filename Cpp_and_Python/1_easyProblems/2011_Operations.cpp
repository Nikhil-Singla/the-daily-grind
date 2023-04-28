// Define a class Solution
class Solution {
public:
    // Define a function finalValueAfterOperations that takes a vector of strings called operations as input and returns an integer
    int finalValueAfterOperations(vector<string>& operations) 
    {
        // Initialize an integer x to 0
        int x = 0;
        // Iterate through each string in operations using a range-based for loop
        for(auto c : operations)
        {
            // Check if the first or second character of the string is a plus sign
            if(c[0] == '+' || c[1] == '+')
            {
                // If so, increment x by 1
                x++;
            }
            else
            {
                // Otherwise, decrement x by 1
                x--;
            }
        }    
        // Return the final value of x
        return x;
    }
};
