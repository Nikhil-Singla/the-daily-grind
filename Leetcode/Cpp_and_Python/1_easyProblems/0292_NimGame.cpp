// Its faster to resolve if-else conditions manually and instruct what to return
// Than it is to return the if-else result.
class Solution {
public:
    bool canWinNim(int n) 
    {
        return (n & 3 ? true : false);    
    }
};

class Solution {
public:
    bool canWinNim(int n) 
    {
        return (n & 3);    
    }
};