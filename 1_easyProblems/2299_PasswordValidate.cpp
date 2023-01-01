class Solution {
public:
    bool strongPasswordCheckerII(string password) 
    {
        string special = "!@#$%^&*()-+";
        bool check[5] = {false};
        if(password.length() < 8)
        {return false;}

        for(int i = 0; i < password.length(); i++)
        {
            if(password[i] >= 'a' && password[i] <= 'z')
            {
                check[0] = true;
                break;
            }
        }

        for(int i = 0; i < password.length(); i++)
        {
            if(password[i] >= 'A' && password[i] <= 'Z')
            {
                check[1] = true;
                break;
            }
        }

        for(int i = 0; i < password.length(); i++)
        {
            if(password[i] >= '0' && password[i] <= '9')
            {
                check[2] = true;
                break;
            }
        }

        for(int i = 0; i < password.length() && !check[3]; i++)
        {
            for(auto &c: special)
            {
                if(password[i] == c)
                {
                    check[3] = true;
                    break;
                }
            }
        }

        check[4] = true;
        for(int i=1; i<password.size(); i++)
        {
            if(password[i-1]==password[i])
            {
                check[4] = false;
                break;
            }
        }

        return(check[0] && check[1] && check[2] && check[3] && check[4]);
    }
};

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