class Solution {
public:
    bool judgeCircle(string moves) 
    {
        int count[2] = {0};
        for(auto c : moves)
        {
            switch(c)
            {
                case 'U':
                    count[0]++; break;
                case 'D':
                    count[0]--; break;
                case 'L':
                    count[1]++; break;
                case 'R': 
                    count[1]--; break;
            }
        }    
        return !(count[0] | count[1]);
    }
};