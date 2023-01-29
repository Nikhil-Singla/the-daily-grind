class Solution {
public:
    bool canPlaceFlowers(vector<int>& flowerbed, int n) 
    {
        int Previous = 0;
        int Next = 0;
        for(int i = 0; i < flowerbed.size(); i++)
        {
            if(i+1 < flowerbed.size())
            {
                Next = flowerbed[i+1];
            }
            else
            {
                Next = 0;
            }

            if(i-1 >= 0)
            {
                Previous = flowerbed[i-1];
            }
            else
            {
                Previous = 0;
            }

            if(!Previous && !Next && !flowerbed[i])
            {
                n--;
                i++;
            }
        }
        return n <= 0;
    }
};