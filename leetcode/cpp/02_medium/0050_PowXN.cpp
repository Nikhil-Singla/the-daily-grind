// Approach by breaking down x into powers of 2.
// Thanks to: Ajna on Leetcode

class Solution {
public:
    double myPow(double x, int n) {
        double ans = 1;
        while (n) 
        {
            if(n % 2) 
            {
                ans = (n > 0 ? ans * x : ans / x);
            }
            x = x * x;
            n /= 2;
        }
        return ans;
    }
};

// REDUNDANT SOLUTION
#include<math.h>
class Solution {
public:
    double myPow(double x, int n) {
        double ans = pow(x,n);
        return ans;
    }
};

// Solution didn't work for very small numbers due to large negative powers.
/* class Solution {
public:
    double myPow(double x, int n) {
        double temp = x;
        if(n > 0)
        {
            for(int i = 1; i < n; i ++)
            {
                x *= temp;
            }
            return x;
        }
        else if(n == 0)
        {
            return 1.0;
        }
        else if(n<0)
        {
            double num = 1;
            int absolute = abs(n);
            for(int i = 1; i < absolute; i++)
            {
                temp *= temp;
            }
            num = (double)num/(double)temp;
            return num;
        }
        return -1.0;
    }
};

*/