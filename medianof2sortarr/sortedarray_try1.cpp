class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) 
    {
        int first=0, first2=0;
        int len1=nums1.size(),len2=nums2.size();
        int flag=1, answer=0;
        vector<int> result;
        while(first<len1)
        {
            if(first2>=len2)
            {
                flag = 2;
                break;
            }
            if(nums1[first]>nums2[first2])
            {
                result.push_back(nums1[first++]);
            }
            else
            {
                result.push_back(nums2[first2++]);
            }
        }
        if(nums1.size()==nums2.size())
        {
            flag = 3;
        }
        if(flag == 1)
        {
            do
            {
                result.push_back(nums1[first]);
            }
            while(++first<len1);
        }
        else if(flag == 2)
        {
            do
            {
                result.push_back(nums2[first2]);
            }
            while(++first2<len2);
        }
        int len3 = len1+len2;
        len3 /= 2;
        if(len3%2==0)
        {
            answer=(result[len3]+result[len3-1])/2;
        }
        else
        {
            answer=result[len3-1];
        }
        return answer;
    }
};
