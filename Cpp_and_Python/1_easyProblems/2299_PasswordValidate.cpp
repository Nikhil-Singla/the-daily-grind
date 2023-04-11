// This is the original code for solving LeetCode Problem 2299, 
// checking if a given password is strong or not
class Solution {
public:
    bool strongPasswordCheckerII(string p) 
    {
        // Define a string of special characters
        string special = "!@#$%^&*()-+";
        // Define an array to check if password contains lower case letters, upper case letters, digits and special characters
        bool chk[5] = {false};
        // If the password length is less than 8 characters, return false
        if(p.length() < 8)
        {return false;}
        // Loop through each character in the password and check if it is a lower case letter
        for(int i = 0; i < p.length(); i++)
        {
            if(p[i] >= 'a' && p[i] <= 'z')
            {chk[0] = true;break;}
        }
        // Loop through each character in the password and check if it is an upper case letter
        for(int i = 0; i < p.length(); i++)
        {
            if(p[i] >= 'A' && p[i] <= 'Z')
            {chk[1] = true;break;}
        }
        // Loop through each character in the password and check if it is a digit
        for(int i = 0; i < p.length(); i++)
        {
            if(p[i] >= '0' && p[i] <= '9')
            {chk[2] = true;break;}
        }
        // Loop through each character in the password and check if it is a special character
        for(int i = 0; i < p.length() && !chk[3]; i++)
        {
            for(auto &c: special)
            {
                if(p[i] == c)
                {chk[3] = true;break;}
            }
        }
        // Check if any adjacent characters in the password are the same
        chk[4] = true;
        for(int i=1; i<p.size(); i++)
        {
            if(p[i-1]==p[i])
            {chk[4] = false;break;}
        }
        // Return true if password contains at least one lower case letter, one upper case letter, one digit, one special character, and no adjacent characters are the same
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