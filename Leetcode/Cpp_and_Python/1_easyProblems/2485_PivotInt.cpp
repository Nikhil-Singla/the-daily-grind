class Solution {
public:
    int pivotInteger(int n) 
    {
        int sum = (n*(n+1))/2;
        int start = 0;
        vector<int> list;
        for(int i = 1; i <= n; i++)
        {
            list.push_back(i);
        }
        for(int i = 0; start <= sum; i++)
        {
            start += list[i];
            if(start == sum)
            {return list[i];}
            sum -= list[i];
            // cout<< start<< " "<< sum<<"\n";
        }    
        return -1;
    }
};