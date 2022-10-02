# include <string>
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        vector<int> hash(256, -1);
        int length = s.length(), result=0, var=0;
        if(length<2)
        {
            return length;
        }
        else if(length == 2)
        {
            if(s.at(0)==s.at(1))
            {return(1);}
            else
            {return 2;}
        }
        auto first=s.begin(), second=s.end();
        auto temp = first+1;
        int ascii=0;
        ascii = int(*first);
        hash[ascii] = 1;
        length = 1;
        while(temp<=second)
        {
            while(*temp!=*first && temp<=second)
            {
                ascii = int(*temp);
                if(hash[ascii]==1)
                {
                    if(result<var)
                    {
                        result = var;
                    }
                    first = temp++;
                    if(*first==*temp)
                    {var = 0;}
                    else
                    {var = 1;}
                }
                hash[ascii] = 1;
                var++;
            }
            if(*first==*temp)
            {var = 0;}
            else
            {var = 1;}
            first = temp++;
        }
        return result;
    }
};

//OLD Code for experience
        /*int len = 0, size=s.size();
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
        return len;*/
