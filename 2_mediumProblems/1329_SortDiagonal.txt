// Faster solution using vector sort.
class Solution {
public:
    vector<vector<int>> diagonalSort(vector<vector<int>>& mat) 
    {
        uint col = mat[0].size(), row = mat.size();
        for(uint i = 0; i < col; i++)
        {
            msort(mat, row, col, 0, i);
        }

        for(uint j = 1; j < row; j++)
        {
            msort(mat, row, col, j, 0);
        }

        return mat;
    }

    void msort(vector<vector<int>>& mat, uint row, uint col, uint i1, uint i2)
    {
        vector<int> holder;
        int temp1 = i1, temp2 = i2;
        while((temp1 < row) && (temp2 < col))
        {
            holder.push_back(mat[temp1][temp2]);
            temp1++; 
            temp2++;
        }

        sort(holder.begin(), holder.end());

        for(auto const c : holder)
        {
            mat[i1][i2] = c;
            i1++; 
            i2++;
        }
    }
};

// Brute force solution using hashmaps
class Solution {
public:
    vector<vector<int>> diagonalSort(vector<vector<int>>& mat) 
    {
        uint col = mat[0].size(), row = mat.size();
        for(uint i = 0; i < col; i++)
        {
            sort(mat, row, col, 0, i);
        }

        for(uint j = 1; j < row; j++)
        {
            sort(mat, row, col, j, 0);
        }

        return mat;
    }

    void sort(vector<vector<int>>& mat, uint row, uint col, uint i1, uint i2)
    {
        map<int, int> count;
        int temp1 = i1, temp2 = i2;
        while((temp1 < row) && (temp2 < col))
        {
            count[mat[temp1][temp2]]++;
            temp1++; 
            temp2++;
        }

        for(int i = 0; i < 101; i++)
        {
            while(count[i]--)
            {
                mat[i1][i2] = i;
                i1++; 
                i2++;
            }
        }
    }
};