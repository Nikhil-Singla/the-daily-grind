// Faster Solution 2
class Solution {
public:
    vector<int> kWeakestRows(vector<vector<int>>& mat, int k) 
    {
        int n = mat[0].size();

        for(int i = 0; i < mat.size(); i++)
        {
            mat[i].push_back(i);
        }

        sort(mat.begin(), mat.end());

        vector<int> ans(k);
        for(int i = 0; i < k; i++)
        {
            ans[i] = mat[i][n];
        }
        return ans;
    }
};

class Solution {
public:
    static bool cmp(const pair<int, int>& a, const pair<int, int>& b)
    {
        if (a.second == b.second)
        {
            return a.first < b.first;
        }
        return a.second < b.second;
    }

    vector<int> kWeakestRows(vector<vector<int>>& mat, int k)
    {
        map<int, int> hash;
        vector<int> ans;
        for (uint i = 0; i < mat.size(); i++)
        {
            uint strength = 0;
            for (auto& d : mat[i])
            {
                if (d)
                {
                    strength++;
                }
                else
                {
                    continue;
                }
            }
            hash[i] = strength;
        }
        vector<pair<int, int>> A;

        for (const auto& it : hash)
        {
            A.push_back(it);
        }

        // Sort using comparator function
        sort(A.begin(), A.end(), cmp);

        // Print the sorted value
        for (int i = 0; i < k; i++)
        {
            ans.push_back(A[i].first);
        }
        return ans;
    }
};