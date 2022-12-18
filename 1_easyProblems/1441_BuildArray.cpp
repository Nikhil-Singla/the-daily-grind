class Solution {
public:
    vector<string> buildArray(vector<int>& target, int n) 
    {
        vector<string> result;
        int stream_counter = 1;
        int i = 0;
        int pop_counter = 0;
        while(i < target.size())
        {   
            if(stream_counter == target[i])
            {
                while(pop_counter > 0)
                {
                    result.push_back("Pop");
                }
                result.push_back("Push");
                i++;
            }
            else
            {
                result.push_back("Push");
                pop_counter++;
            }
            stream_counter++;
        }   
        return result; 
    }
};