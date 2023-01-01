class Solution {
public:
    bool strongPasswordCheckerII(string p) 
    {
        string special = "!@#$%^&*()-+";
        bool chk[5] = {false};
        if(p.length() < 8)
        {return false;}
        for(int i = 0; i < p.length(); i++)
        {
            if(p[i] >= 'a' && p[i] <= 'z')
            {chk[0] = true;break;}
        }
        for(int i = 0; i < p.length(); i++)
        {
            if(p[i] >= 'A' && p[i] <= 'Z')
            {chk[1] = true;break;}
        }
        for(int i = 0; i < p.length(); i++)
        {
            if(p[i] >= '0' && p[i] <= '9')
            {chk[2] = true;break;}
        }
        for(int i = 0; i < p.length() && !chk[3]; i++)
        {
            for(auto &c: special)
            {
                if(p[i] == c)
                {chk[3] = true;break;}
            }
        }
        chk[4] = true;
        for(int i=1; i<p.size(); i++)
        {
            if(p[i-1]==p[i])
            {chk[4] = false;break;}
        }
        return(chk[0] && chk[1] && chk[2] && chk[3] && chk[4]);
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