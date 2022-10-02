class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) 
    {
        auto start1=nums1.begin(),start2=nums2.begin();
        auto end1=nums1.end(),end2=nums2.end();
        int len=nums1.size()+nums2.size();
        vector<int> nums;
        double answer=3;
        end1--;
        end2--;
        for(int i = 0;((start1<=end1)&&(start2<=end2));i++)
        {
            if(*start2>*start1)
            {
                nums.push_back(*start1);
                start1++;
            }
            else
            {
                nums.push_back(*start2);
                start2++;
            }
        }
        while(start1<=end1)
        {
            nums.push_back(*start1);
            start1++;
        }
        while(start2<=end2)
        {
            nums.push_back(*start2);
            start2++;
        }
        /* for (int i = 0; i < nums.size(); i++) 
        {
            cout << nums[i] << " ";
        }
        cout << endl; */
        // cout<<len;
        if(len%2==0)
        {
            answer=(double)nums[(len/2)-1]+(double)nums[(len/2)];
            answer /= 2;
        }
        else
        {
            answer=(double)nums[(len/2)];
        }
        return answer;
    }
};
