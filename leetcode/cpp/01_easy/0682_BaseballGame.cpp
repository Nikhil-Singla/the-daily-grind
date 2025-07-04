class Solution {
public:
    int calPoints(vector<string>& operations) 
    {
        int tempStorageOne;
        int tempStorageTwo;
        int finalSum = 0;
        stack<int> scoreStack;
        
        for(string i : operations)
        {
            if(i == "C")
            {
                scoreStack.pop();
            }
            else if(i == "D")
            {
                scoreStack.push(scoreStack.top()*2);
            }
            else if(i == "+")
            {
                tempStorageOne = scoreStack.top();
                scoreStack.pop();
                tempStorageTwo = scoreStack.top();
                scoreStack.push(tempStorageOne);
                scoreStack.push(tempStorageOne + tempStorageTwo);
            }
            else
            {
                scoreStack.push(stoi(i)); //stoi() to convert string into integer 
            }
        }
        
        while(scoreStack.size() != 0)
        {
            finalSum += scoreStack.top();
            scoreStack.pop();
        }

        return finalSum;
    }
};