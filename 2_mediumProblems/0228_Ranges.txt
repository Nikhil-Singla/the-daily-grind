class Solution {
public:

    string rangePush(int a, int b)
    {
        stringstream stream1, stream2;
        stream1 << a;
        string num1 = stream1.str();
        if(a == b)
        {
            return num1;
        }
        stream2 << b;
        string num2 = stream2.str();
        return (num1+"->"+num2);
    }

    vector<string> summaryRanges(vector<int>& nums) 
    {
        vector<string> ans;
        if(nums.size() < 1)
        {
            return ans;
        }
        int start = 0, end = 0;
        for(int i = 1; i < nums.size(); i++)
        {
            if(nums[end] + 1 == nums[i])
            {
                end = i;
            }
            else
            {
                ans.push_back(rangePush(nums[start], nums[end]));
                start = i;
                end = i;
            }
        }
        ans.push_back(rangePush(nums[start], nums[end]));
        return ans;
    }
};