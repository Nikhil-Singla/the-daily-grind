# include <string>
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int len = 0, size=s.size();
        string::iterator first, second, last;
        first = s.begin();
        second = first+1;
        last = s.end()-2;
        int temp = 0;
        int furst = -1, seconduh = -1;
        while(second <= last)
        {
            temp = 1;
            // std::cout<<*first;
            vector<pair<int,int>> hash_set(256, -1);
            furst = *first;
            seconduh = *second;
            hash_set[furst] = 1;
            hash_set[seconduh] = 1;
            while((hash_set[*second]!=1) && (second<=last))
            {
                hash_set[*second] = 1;
                ++temp;
                ++second;
                std::cout<<*second;
            }
            ++second;
            // std::cout<<*second;
            first = second;
            if(len<temp)
            {
                len = temp;
            }
        }
        return len;
    }
};
