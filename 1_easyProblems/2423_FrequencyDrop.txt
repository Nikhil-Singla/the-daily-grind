class Solution {
public:
    bool isEqual(string str, int index)
    {
        str.erase(index, 1);  //erasing i'th element 
        int alpha[26] = {0}; 
        
        for (auto c : str)  
        {
            alpha[c-'a']++;
        }        
        int count = 0;
        for (int i = 0; i < 26; i++)
        {
            if(alpha[i] == 0) {continue;}
            if(!count) {count = alpha[i];}
            if(alpha[i] != count) {return false;}
        }
        return true;
    }
    bool equalFrequency(string word) {
        for (int i = 0; i < word.size(); i++)
        {if (isEqual(word, i)) return true;	}	
        return false;
    }
};