class Solution {
public:
    vector<int> plusOne(vector<int>& digits) 
    {
        if(digits.back() != 9)
        {
            digits.back()++;
            return digits;
        }
        vector<int> cpy;
        cpy.assign(digits.begin(), digits.end());
        reverse(cpy.begin(), cpy.end());
        cpy.push_back(0);
        int itr = 0;
        while(true)
        {
            if(cpy[itr] != 9)
            { 
                cpy[itr]++;
                break;
            }
            else
            {
                cpy[itr] = 0;
                itr++;
            }
        }
        if(cpy.back() == 0)
        {
            cpy.pop_back();
        }
        reverse(cpy.begin(), cpy.end());
        return cpy;
    }
};