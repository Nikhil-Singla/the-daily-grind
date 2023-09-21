class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) 
    {
        int n = nums1.size();
        int m = nums2.size();
        int i = 0, j = 0, firstVal = 0, secondVal = 0;

        for (int currIndex = 0; currIndex <= (n+m)/2; currIndex++)
        {
            secondVal = firstVal;
            if(i != n && j != m)
            {
                (nums1[i] > nums2[j] ? firstVal = nums2[j++] : firstVal = nums1[i++]);
            }
            else if(i < n)
            {
                firstVal = nums1[i++];
            }
            else
            {
                firstVal = nums2[j++];
            }
        }

        if((n+m)%2 == 1)
        {
            return firstVal;
        }    
        else
        {
            return (firstVal+secondVal) / 2.0;
        }
    }
};