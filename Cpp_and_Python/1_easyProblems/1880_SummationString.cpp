class Solution {
public:
    
    int toInt(vector<int> arr)
    {
        int res = 0;
        for(auto c : arr)
        {
            res += c;
            res *= 10;
        }
        return res;
    }

    vector<int> numerateString(string given)
    {
        vector<int> result;
        for(auto c : given)
        {
            result.push_back(c - 'a');
        }
        return result;
    }
    
    bool isSumEqual(string firstWord, string secondWord, string targetWord) 
    {
        vector<int> first, second, target;
        first = numerateString(firstWord);
        second = numerateString(secondWord);
        target = numerateString(targetWord);
        int summation = 0, want = 0;
        summation = toInt(first) + toInt(second);
        want = toInt(target);
        if(summation == want)
        {
            return true;
        }
        return false;
    }
};