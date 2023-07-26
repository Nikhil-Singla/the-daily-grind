class NumArray {
public:

    vector<int> S;

    NumArray(vector<int>& nums) : S(nums) 
    {
        for(int i = 1; i < S.size(); i++)
        {
            S[i] += S[i-1];
        }
        
        //for(auto c: S)
        //{
        //    cout<<c<<" ";
        //}
    }
    
    int sumRange(int left, int right) 
    {
        if (left == 0) 
        {
            return S[right];
        }
        return S[right] - S[left-1];
    }
};

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray* obj = new NumArray(nums);
 * int param_1 = obj->sumRange(left,right);
 */