// Solution that solves the problem using mathematics and logic

class Solution {
public:

    int uniquePaths(int m, int n) 
    {
        int highest = max(m,n);
        if(m == 1 || n == 1)
        {
            return 1;
        } 
        
        int maze[m][n];
        for(int i = 0; i < m; i++)
        {
            maze[i][0] = 1;
        }
        for(int i = 0; i < n; i++)
        {
            maze[0][i] = 1;
        }

        for(int i = 1; i < m; i++)
        {
            for(int j = 1; j < n; j++)
            {
                maze[i][j] = maze[i-1][j] + maze[i][j-1];
            }
        }
        return maze[m-1][n-1];
    }



// Initial Solution that exceeds time limit

class Solution {
public:
    int uniquePaths(int m, int n, int i = 0, int j = 0) 
    {
        if(i >= m || j >= n) {return 0;}                                   
        if(i == m-1 && j == n-1) {return 1;}                                
        return (uniquePaths(m, n, i+1, j) + uniquePaths(m, n, i, j+1));     
    }
};

