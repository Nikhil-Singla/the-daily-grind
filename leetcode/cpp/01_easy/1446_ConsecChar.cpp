class Solution {
public:
    int maxPower(string s) 
    {
        // Initialize variables to keep track of the current and maximum sequence length
        unsigned short c = 1, a = 1;
        
        // Loop through the string, starting from the second character
        for(unsigned short i = 1; i < s.length(); i++)
        {
            // If the current character is the same as the previous character, increase the sequence length
            if(s[i] == s[i-1])
            {
                c++;
                
                // Update the maximum sequence length if necessary
                if(c > a) {a = c;}
            } 
            // If the current character is different from the previous character, reset the sequence length to 1
            else c = 1;
        }    
        // Return the maximum sequence length
        return a;
    }
};
