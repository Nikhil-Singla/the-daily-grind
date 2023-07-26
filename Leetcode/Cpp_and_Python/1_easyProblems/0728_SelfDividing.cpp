class Solution {
public:
    vector<int> selfDividingNumbers(int left, int right) 
    {
        vector<int> result;
        for(int i=left; i<=right; i++)
        {    
            int temp = i;
            while(temp > 0)
            {
                int check = temp%10;
                if(check==0 || i%check!=0) {break;}
                temp /= 10;
            }
            if(temp==0) {result.push_back(i);}
        }
        return result;
    }
};