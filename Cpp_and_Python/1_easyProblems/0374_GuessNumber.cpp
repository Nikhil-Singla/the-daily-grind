/** 
 * Forward declaration of guess API.
 * @param  num   your guess
 * @return 	     -1 if num is higher than the picked number
 *			      1 if num is lower than the picked number
 *               otherwise return 0
 * int guess(int num);
 */

class Solution {
public:
    int guessNumber(int n) 
    {
        uint sol = n/2;
        uint low = 1;
        while(low < n)
        {
            switch(guess(sol))
            {
                case -1 : 
                    n = sol-1;
                    break;
                case 0 :
                    return sol;
                    break;
                case 1 :
                    low = sol+1;
                    break;
            }
            sol = (n+low)/2;
        }    
        return n;
    }
};