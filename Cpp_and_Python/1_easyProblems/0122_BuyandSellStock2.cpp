/*
Leetcode problem 122: Best Time to Buy and Sell Stock II

Problem statement: Given an array of stock prices for each day, find the maximum profit that can be obtained by buying and selling multiple times. 

Solution approach: We can iterate through the array of prices, and for each pair of consecutive prices where the second price is greater than the first, 
we can add the difference to the total profit. This is because buying at the first price and selling at the second price will result in a profit equal 
to the difference between the prices. By doing this for all pairs of consecutive prices where the second price is greater than the first, we can obtain 
the maximum profit that can be obtained by buying and selling multiple times.

*/

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int maxProfit = 0; // Initialize the variable to store the maximum profit to 0
        for(int i = 1; i < prices.size(); i++) // Loop through the prices array, starting from the second element
        {
            if(prices[i] > prices[i-1]) // If the current price is greater than the previous price
            {
                maxProfit += prices[i] - prices[i-1]; // Add the difference to the maximum profit
            }
        }
        return maxProfit; // Return the maximum profit
    }
};
