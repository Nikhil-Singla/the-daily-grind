class Solution {
public:
    void sortColors(vector<int>& nums) 
    {
        int low = 0, high = nums.size()-1, itr = 0;
        while(itr <= high)
        {
            switch(nums[itr])
            {
                case 0: 
                    swap(nums[low], nums[itr]);
                    low++; itr++; 
                    break;
                case 2: 
                    swap(nums[high], nums[itr]);
                    high--; 
                    break;
                case 1: 
                    itr++; 
                    break;
            }
        }    
    }
};

//If Else statements
class Solution {
public:
    void sortColors(vector<int>& nums) 
    {
        int low = 0, high = nums.size()-1, itr = 0;
        if(nums.size() < 2)
        {
            return;
        }
        while(itr <= high)
        {
            if(nums[itr] == 0)
            {
                swap(nums[low], nums[itr]);
                low++; itr++; 
            }
            else if(nums[itr] == 2) 
            {
                swap(nums[high], nums[itr]);
                high--;
            }
            else 
            {
                itr++; 
            }
        }    
    }
};
