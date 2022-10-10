class Solution {
public:
    bool isPalindrome(int x) {
        vector<int> num;
        unsigned long int count = 0, temp = x;
        if(x < 0)
        {
            return false;
        }
        while(temp != 0)
        {
            count *= 10;
            count += (temp%10);
            temp /= 10;
            // cout<<count<<" ";
        }
        if(count == x)
        {return true;}
        else
        {return false;}
    }
};
