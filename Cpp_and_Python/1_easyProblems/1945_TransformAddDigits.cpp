class Solution {
public:
    int getLucky(string s, int k) 
    {
        int sum = 0;
        k--;
        for(int i = 0; i < s.length(); i++)
        {
            char temp = s[i];
            int num_form = temp - 96; 
            while(num_form != 0)
            {
                sum += num_form%10;
                num_form /= 10;
            }
        }
        while(k--)
        {
            int helper = 0;
            while(sum)
            {
                helper += sum%10;
                sum = sum/10;
            }
            sum = helper;
        }
        return sum;
    }
};