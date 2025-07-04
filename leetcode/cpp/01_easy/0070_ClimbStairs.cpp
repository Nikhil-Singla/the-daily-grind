/*
Leetcode Problem 70: Climbing Stairs

Problem statement: You are climbing a staircase. It takes n steps to reach the top. Each time you can either climb 1 or 2 steps. 
In how many distinct ways can you climb to the top?

The climbing stairs is essentially the fibonacci sequence
one step means you can add 1 to each of the one step ago.
two step means you can add 2 to each of the two step ago.
So total new steps -> all 1 steps ago + all 2 steps ago

Solution approach: This is a classic problem of dynamic programming. We can solve it by breaking it down into smaller subproblems and storing 
the solutions to these subproblems in an array. Specifically, we can define a vector to store the number of distinct ways to reach each step 
of the staircase, starting from step 0 (which we define to be 0). We can then use a for loop to iterate through the steps, filling in the number 
of distinct ways to reach each step based on the number of distinct ways to reach the previous two steps.

For example, to reach step i, we can either climb 1 step from step i-1, or 2 steps from step i-2. Therefore, the number of distinct ways to reach step i 
is the sum of the number of distinct ways to reach steps i-1 and i-2.

We also include base cases to handle the cases where n is less than or equal to 0, 1, or 2.

*/

class Solution {
public:
    int climbStairs(int n) // function to determine the number of distinct ways to climb a staircase with n steps
    {
        vector<int> ans(n+1, 0); // define a vector to store the number of distinct ways to reach each step, starting from step 0 (which we define to be 0)

        // base cases
        if(n <= 0) return 0; // if there are 0 or fewer steps, there are 0 distinct ways to climb
        if(n == 1) return 1; // if there is 1 step, there is only 1 distinct way to climb (climbing 1 step)
        if(n == 2) return 2; // if there are 2 steps, there are 2 distinct ways to climb (climbing 2 steps or climbing 1 step twice)

        ans[0] = 0; // define the number of distinct ways to reach step 0 as 0
        ans[1] = 1; // define the number of distinct ways to reach step 1 as 1
        ans[2] = 2; // define the number of distinct ways to reach step 2 as 2

        for(int i=3; i<=n; i++) // iterate through the steps, starting from step 3
        {
            ans[i] = ans[i-1] + ans[i-2]; // the number of distinct ways to reach step i is the sum of the number of distinct ways to reach steps i-1 and i-2
        }
        return ans[n]; // return the number of distinct ways to reach the top (i.e., step n)
    }
};

// Alternate Method
class Solution {
public:

    int climbStairs(int n) 
    {
        vector<int> ans;
        ans.push_back(0);
        ans.push_back(1);
        ans.push_back(2);
        for(int i = 3; i <= n; i++)
        {
            ans.push_back(ans[i-1] + ans[i-2]);
        }    
        return ans[n];
    }
};

// Slower due to one error in solution
class Solution {
public:

    vector<int> ans;
    
    int climbStairs(int n) 
    {
        ans.push_back(0);
        ans.push_back(1);
        ans.push_back(2);
        for(int i = 3; i <= n; i++)
        {
            ans.push_back(ans[i-1] + ans[i-2]);
        }    
        return ans[n];
    }
};