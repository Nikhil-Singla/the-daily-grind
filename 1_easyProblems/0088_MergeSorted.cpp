class Solution {
public:
    void merge(vector<int>& nums1, int length_main, vector<int>& nums2, int length_side) 
    {
        if(length_main == 0)
        {
            for(int i = 0, j = 0; j<length_side; j++)
            {
                nums1[i++] = nums2[j];
            }
            return;
        }
        
        if(length_side == 0)
        {
            return;
        }

        int temp = length_main;
        for(int i = 0; i < length_side; i++)
        {
            nums1[temp++] = nums2[i];
        }
        sort(nums1.begin(), nums1.end());
    }
};