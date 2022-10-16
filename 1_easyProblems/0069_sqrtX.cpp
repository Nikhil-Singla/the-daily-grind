class Solution {
public:
    int mySqrt(int x) {
        int start = 0, last = x;
        int mid = 0, square = 0;
        if(x==0)
        {return 0;}
        if(x == 1)
        {return 1;}
        while(start<last)
        {
            mid = (start+last)/2;
            square = mid*mid;
            if(square < x)
            {
                start = mid+1;
            }
            if(square > x)
            {
                last = mid;
            }
            if(square == x)
            {
                return mid;
            }
        }
        start -= 1;
        return start;
    }
};