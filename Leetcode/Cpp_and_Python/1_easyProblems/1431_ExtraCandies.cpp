// This is a solution to Leetcode Problem 1431: Kids With the Greatest Number of Candies
class Solution {
public:
    // This function takes in a vector of integers representing the number of candies each kid has,
    // and an integer representing the extra candies that can be given to any kid.
    // It returns a vector of boolean values indicating whether each kid can have the greatest number of candies.
    vector<bool> kidsWithCandies(vector<int>& candies, int extraCandies) 
    {
        // This variable keeps track of the highest number of candies among all the kids.
        int highest = 0;
        // This loop iterates through all the kids' candies and updates the highest variable if necessary.
        // It also adds the extra candies to each kid's candies.
        for(auto &c : candies)
        {
            highest = max(highest, c);
            c += extraCandies; 
        }
        // This vector will store the boolean results indicating whether each kid can have the greatest number of candies.
        vector<bool> result;
        // This loop iterates through all the kids' candies and checks if each kid has the greatest number of candies.
        // It then appends the result to the result vector.
        for(auto c : candies)
        {
            if(c >= highest)
            {
                result.push_back(true);
            }
            else
            {
                result.push_back(false);
            }
        }
        // Finally, the function returns the result vector.
        return result;
    }
};
