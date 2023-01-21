class Solution {
public:
    vector<string> restoreIpAddresses(string inputString) 
    {
        vector<string> Ans;
        if(inputString.size() < 4) {return Ans;}
        helperFunction(0, 0, "", Ans, inputString);
        return Ans;
    }

    bool isValid(string StringToCheck)
    {
        if(StringToCheck.size() > 3 || StringToCheck.size() == 0)
        {return false;}
        if((StringToCheck.size() > 1) && StringToCheck[0] == '0')
        {return false;}   
        if(StringToCheck.size() && stoi(StringToCheck) > 255)
        {return false;}
        return true;
    }

    void helperFunction(int CurrIndex, int NumberOfDots, string TempSubStr, vector<string>&Ans, string originalString)
    {
        if(NumberOfDots == 3)
        {                
            if(isValid(originalString.substr(CurrIndex)))
            {
                Ans.push_back(TempSubStr+originalString.substr(CurrIndex));   
            }
            return;
        }

        for(int RecursiveIndex = CurrIndex; RecursiveIndex < originalString.size(); RecursiveIndex++)
        {
            if( isValid( originalString.substr( CurrIndex, (RecursiveIndex-CurrIndex)+1 ) ) )
            {
                TempSubStr.push_back(originalString[RecursiveIndex]);
                TempSubStr.push_back('.');
                helperFunction(RecursiveIndex+1, NumberOfDots+1, TempSubStr, Ans, originalString);
                TempSubStr.pop_back();
            }
        }
        return;
    }
};