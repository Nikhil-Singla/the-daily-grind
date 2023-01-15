class Solution {
public:
    bool isPerfectSquare(int num) 
    {
        if(num == 1)
        {return true;}

        unsigned long int start = 0;
        unsigned long int end = num;

        while(start <= end)
        {
            unsigned long int mid = (start + end)/2;
            unsigned long int square = mid*mid;
            if(square == num)
            {
                return true;
            }

            if(square < num)
            {
                start = mid+1;
            }
            else
            {
                end = mid-1;
            }
        }
        return false;
    }
};