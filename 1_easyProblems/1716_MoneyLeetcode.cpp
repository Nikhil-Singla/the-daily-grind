class Solution {
public:
    int totalMoney(int n) 
    {
        int result = 0;
        int week = 1;
        int day = 0;
        for(int i = 0; i < n; i++, day++)    
        {
            result += (week + day);
            cout<<week+day<<" ";
            if( day%6 == 0 && day !=0)
            {
                day = -1;
                week++;
            }
        }
        return result;
    }
};