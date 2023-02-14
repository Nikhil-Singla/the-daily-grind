class Solution {
public:
    int countDigits(int num) 
    {
        int temp = num;
        vector<int> map;
        while(temp)
        {
            map.push_back(temp%10);
            temp /= 10;
        }    
        uint count = 0;
        for(auto c : map)
        {
            if(!(num%c))
            {
                count++;
            } 
        }
        return count;
    }
};