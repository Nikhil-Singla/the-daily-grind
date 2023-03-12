class Solution {
public:
    bool checkIfExist(vector<int>& arr) {
        unordered_map<int, int> hash;
        int flag = -1;
        for(int i = 0; i<arr.size(); i++)
        {
            hash[arr[i]] += 1;
            if(arr[i] ==  0)
            {
                flag = i;
            }
        }
        for(int i = 0; i<arr.size(); i++)
        {

            if(hash[2*arr[i]] > 0 && (flag != i))
            {
                return true;
            }
        }
        return false;
    }
};

// Alternate Solution: BRUTE FORCE

class Solution {
public:
    bool checkIfExist(vector<int>& arr) 
    {
        for(int i = 0; i < arr.size(); i++)
        {
            for(int j = i+1; j < arr.size(); j++)
            {
                if(arr[i] == 2 * arr[j] || arr[j] == 2 * arr[i])
                {return 1;}
            }
        }
    return 0;
    }
};