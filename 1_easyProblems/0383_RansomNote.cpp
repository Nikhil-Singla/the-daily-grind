class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) 
    {
        for(auto c : ransomNote)
        {
            if(magazine.find(c) == string::npos)
            {
                return false;
            } 
            else
            {
                magazine.erase(magazine.find(c), 1);
            }
        }    
        return true;
    }
};