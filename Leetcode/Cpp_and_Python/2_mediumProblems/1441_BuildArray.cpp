class Solution {
public:
    vector<string> buildArray(vector<int>& target, int n) 
    {
        vector<string> result;
        int stream_counter = 1;
        int i = 0;
        while(i < target.size())
        {   
            result.push_back("Push");
            if(stream_counter != target[i])
            {
                result.push_back("Pop");
            }
            else
            {
                i++;
            }
            stream_counter++;
        }   
        return result; 
    }
};