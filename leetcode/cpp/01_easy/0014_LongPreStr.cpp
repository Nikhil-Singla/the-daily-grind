/** 
The longestCommonPrefix function takes a vector of strings as input and returns the longest common prefix of all the strings.
**/

class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) 
    {
        // Sort the input vector of strings in ascending order
        sort(strs.begin(), strs.end());

        // Determine the number of strings in the input vector
        uint n = strs.size();

        // Initialize an empty string for the common prefix
        string ans = "";

        // Iterate over each character in the first and last strings of the sorted vector
        for(int i = 0; (i < strs[n-1].length()) && (i < strs[0].length()); i++)
        {
            // If the current character is the same in both strings, add it to the common prefix
            if(strs[n-1][i] == strs[0][i])
            {
                ans += strs[n-1][i];
            }
            // Otherwise, break out of the loop since the common prefix has ended
            else
            {
                break;
            }
        }    

        // Return the common prefix
        return ans;
    }
};
