class Solution {
public:
    int missingNumber(vector<int>& nums) 
    {
        uint array_Sum = 0, sum = 0, i = 0;
        for(auto const c : nums)
        {
            array_Sum += c;
            sum += i++;
        }    
        sum += i;
        return sum - array_Sum;
    }
};

class Solution {
public:
    int missingNumber(vector<int>& nums) 
    {
        unordered_map<int, bool> hash;
        for(auto& c : nums)
        {
            hash[c] = true;
        }    
        for(int i = 0; i <= nums.size(); i++)
        {
            if(hash[i])
            {}
            else
            {
                return i;
            }
        }
        return 1;
    }
};