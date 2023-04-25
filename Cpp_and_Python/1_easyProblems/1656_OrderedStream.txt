class OrderedStream {
public:

    int pointer, count;
    vector<string> customstream;

    OrderedStream(int n) : customstream(n, "1") 
    {
        pointer = 0;
        count = n;
    }

    vector<string> insert(int idKey, string value) 
    {
        customstream[idKey-1] = value;
        vector<string> ans;
        while(pointer < count && customstream[pointer] != "1")
        {
            ans.push_back(customstream[pointer++]);
        }    
        return ans;
    }
};

/**
 * Your OrderedStream object will be instantiated and called as such:
 * OrderedStream* obj = new OrderedStream(n);
 * vector<string> param_1 = obj->insert(idKey,value);
 */