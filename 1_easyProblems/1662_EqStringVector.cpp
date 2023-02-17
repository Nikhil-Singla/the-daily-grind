class Solution {
public:
    bool arrayStringsAreEqual(vector<string>& word1, vector<string>& word2) 
    {
        string one = "", two = "";
        for(auto c : word1)
        {
            one += c;
        }    
        for(auto c : word2)
        {
            two += c;
        }    
        return (one == two);
    }
};