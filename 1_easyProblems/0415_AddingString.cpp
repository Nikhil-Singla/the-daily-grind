class Solution {
public:
    string addStrings(string num1, string num2) 
    {
        int i = num1.length()-1, j = num2.length()-1;
        int carry = 0;
        string ans;
        while(i >= 0 || j >= 0 || carry)
        {
            int a = 0, b = 0;
            if(i >= 0) 
            {
                a = num1[i] - '0';
                i--;
            }
            if(j >= 0)
            {
                b = num2[j] - '0';
                j--;
            }
            int sum = a + b + carry;
            carry = sum/10;
            sum = sum%10;
            ans = to_string(sum) + ans;
        }
        return ans;
    }
};