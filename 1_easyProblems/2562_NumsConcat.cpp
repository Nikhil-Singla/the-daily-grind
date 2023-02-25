class Solution {
public:

    int digits(int number)
    {
        int factor = 10;
        while(number)
        {
            number /= 10;
            factor *= 10;
        }
        return factor/10;
    }

    long long findTheArrayConcVal(vector<int>& nums) 
    {
        long long ans = 0;
        for(int i = 0; i < nums.size(); i++)
        {
            if(i == nums.size()-1)
            {
                ans += nums[i];
                break;
            }
            ans += nums[i]*digits(nums.back()) + nums.back();
            nums.pop_back();
        }    
        return ans;
    }
};