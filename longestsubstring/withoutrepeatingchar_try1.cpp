//After a whole bunch of mindtrickery, finally got around to getting a working solution with a lot of help.
//Sliding Window Solution
# include <string>
class Solution {
public:
    int lengthOfLongestSubstring(string str) {
        unordered_map<char, int>map; //Creates a map of characters, where the key is a char and it points to a value.
        int maxlen = 0; //Initializing the result
        for(int point1 = 0, point2 = 0; point2 < str.size(); point2++) //Our second "pointer" moves down the array
        {
            map[str[point2]]++; //As our pointer gets a character in the string, we increment the value of that character
                                //in the map by 1
            while(map[str[point2]] > 1) //If at any point the value of the character hits 2, it means we have reached a repeated character which we need to resolve by the sliding window.
            {
                map[str[point1++]]--; //Now we move our window frame up, and decrement all the values we pass as they are removed from the frame.
            }
            maxlen = max(maxlen, point2 - point1 + 1); //We find if our current length is higher, or the old one. The +1 is because we need to count the initial starting point in the length (I think)
        }
        return maxlen; //Return the max value
    }
};
