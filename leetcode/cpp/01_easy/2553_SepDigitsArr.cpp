// Faster code
class Solution {
public:
    vector<int> separateDigits(vector<int>& nums) 
    {
        vector<int> result;
        for(auto c : nums)
        {
            string s = to_string(c);
            for(auto d : s)
            {
                result.push_back(d - '0');
            }
        }
        return result;
    }
};


// Brute force solution
class Solution {
public:
    vector<int> separateDigits(vector<int>& nums) 
    {
        vector<int> result;
        for(auto c : nums)
        {
            vector<int> temp;
            while(c)
            {
                temp.push_back(c%10);
                c /= 10;
            }
            while(temp.size())
            {
                result.push_back(temp.back());
                temp.pop_back();
            }
        }
        return result;
    }
};