class Solution {
public:
    int maximumCount(vector<int>& nums) 
    {
        int n = nums.size();
        int negatives = 0;
        for(auto c : nums)
        {
            if(c > 0) {break;}
            if(c < 0) {negatives++;}
            if(c == 0) {n--;}
        }
        return max(negatives, n - negatives);
    }
};