// Faster code by making it a function instead of storing it.
class Solution {
public:

    int map(char s) 
    {
        switch(s) 
        {
            case 'I': return 1;
            case 'V': return 5;
            case 'X': return 10;
            case 'L': return 50;
            case 'C': return 100;
            case 'D': return 500;
            case 'M': return 1000;
            default: return 0;
        }
        return 0;
    }
    int romanToInt(string s) 
    {
        int sum = 0, n = s.length();
        for(int i = 0; i < n - 1; i++)
        {
            int next = map(s[i+1]);
            int curr = map(s[i]);
            if(next > curr)
            {
                sum -= curr;
            }
            else
            {
                sum += curr;
            }
        }
        sum += map(s[n-1]);
        return sum;
    }
};

// Slower Code
class Solution {
public:
    int romanToInt(string s) 
    {
        unordered_map<char, int> map;
        map['I'] = 1;     
        map['V'] = 5;
        map['X'] = 10;
        map['L'] = 50;
        map['C'] = 100;
        map['D'] = 500;
        map['M'] = 1000;
        int sum = 0, n = s.length();
        for(int i = 0; i < n - 1; i++)
        {
            int next = map[s[i+1]];
            int curr = map[s[i]];
            if(next > curr)
            {
                sum -= curr;
            }
            else
            {
                sum += curr;
            }
        }
        sum += map[s[n-1]];
        return sum;
    }
};