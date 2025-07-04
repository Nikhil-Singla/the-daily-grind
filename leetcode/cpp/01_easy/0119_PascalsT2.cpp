/*
Leetcode problem 119: Pascal's Triangle II

Problem statement: Given an index k, return the kth row of the Pascal's triangle.

Solution approach: We can construct the Pascal's triangle row by row, where each row can be calculated from the previous row. We start with 
the first row, which is simply the number 1. For each subsequent row, we first create a vector of size i+1 (where i is the current row index), 
and set the first and last elements to 1. For the remaining elements, we can use the previous row to calculate them using the formula 
row[j] = prev_row[j-1] + prev_row[j]. We repeat this process until we have constructed the kth row of the Pascal's triangle.

*/

class Solution {
public:
    vector<int> getRow(int n) // n is the index of the row we want to retrieve
    {
        vector<vector<int>> v; // Create a 2D vector to store the rows of Pascal's triangle
        v.push_back({1}); // Initialize the first row to be {1}
        for(uint i = 1; i <= n; i++) // Iterate from 1 up to n
        {
            vector<int> row(i+1); // Create a new row vector of size i+1
            row[0] = 1; // Set the first element to 1
            row[i] = 1; // Set the last element to 1
            for(uint j = 1; j < i; j++) // Iterate from 1 up to i-1
            {
                row[j] = v[i-1][j-1] + v[i-1][j]; // Calculate the value of the current element using the previous row
            }
            v.push_back(row); // Add the current row to the 2D vector
        }
        return v.back(); // Return the last row of the 2D vector (i.e. the kth row of Pascal's triangle)
    }
};
