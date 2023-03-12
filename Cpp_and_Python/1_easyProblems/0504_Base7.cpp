class Solution {
public:
    string convertToBase7(int num) 
    {
        if(!num)
        {return "0";}
        string ans = "";
        bool flag = false;
        if(num < 0) {flag = true;}
        while(num)
        {
            ans = to_string(abs(num)%7) + ans;
            num /= 7;
        } 
        if(flag) {ans = '-' + ans;}
        return ans;
    }
};