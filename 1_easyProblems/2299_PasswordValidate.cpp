class Solution {
public:
    bool strongPasswordCheckerII(string password) 
    {
        int len = password.length();

        if(len < 8)
        {return false;}   

        bool checker[4] = {false};
        int count[128] = {0};

        char temp = password[0];
        count[temp]++;

        for(int i = 1; i < len; i++)
        {
            if(temp == password[i])
            {
                return false;
            }
            temp = password[i];
            count[temp]++;
        }

        for(int i = 'a'; i <= 'z'; i++)
        {
            if(count[i] > 0)
            {
                checker[0] = true;
            }
        }
        for(int i = 'A'; i <= 'Z'; i++)
        {
            if(count[i] > 0)
            {
                checker[1] = true;
            }
        }
        for(int i = '0'; i <= '9'; i++)
        {
            if(count[i] > 0)
            {
                checker[2] = true;
            }
        }
        string special = "!@#$%^&*()-+";
        for(auto &c : special)
        {
            if(count[c] > 0)
            {
                checker[3] = true;
            }
        }
        return (checker[0] && checker[1] && checker[2] && checker[3]);
    }
};