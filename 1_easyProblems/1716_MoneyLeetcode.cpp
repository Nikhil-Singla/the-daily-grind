// Code to calculate the money in the bank
class Solution {
public:
    int totalMoney(int n) 
    {
        int result = 0;     //Variable used to store the final amount
        int week = 1;       //What week we are on
        int day = 0;        //What day of the week we are on
        for(int i = 0; i < n; i++, day++)   //Loop to calculate n times.
        {
            result += (week + day);         //Add the money to the result
            cout<<week+day<<" ";
            if( day%6 == 0 && day !=0)      //Reset the week
            {
                day = -1;                   //Start from -1 because day++
                week++;                     //Week changes to next one
            }
        }
        return result;
    }
};