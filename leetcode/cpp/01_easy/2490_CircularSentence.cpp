class Solution {
public:
    bool isCircularSentence(string sentence) 
    {
        char first = sentence[0];
        char last = sentence[sentence.length()-1]; 
        bool flag = (first == last);
        for(int i = 0; i < sentence.length()-1; i++)
        {
            if(sentence[i] == ' ')
            {
                if(sentence[i-1] != sentence[i+1])
                {return false;}
            }
        }    
        return (true && flag);
    }
};