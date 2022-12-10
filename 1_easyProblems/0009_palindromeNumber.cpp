// Program to find if a given number is a palindrome or not
class Solution {
public:

    // Function takes integer x and returns true if number is palindrome and false otherwise.
    bool isPalindrome(int x) 
    {
        // Datatype is unsigned long int because reversal numbers might become too large for standard int
        unsigned long int count = 0, temp = x;
        // count is a number used to keep track of the reverse of x
        // temp is a number that will be worked on instead of x so that
        // we can use x later in comparison
        
        if(x < 0)
        {
            return false;           // Base case of x being negative as negative numbers are non-palindromic
        }
        
        while(temp != 0)    
        // When temp becomes 0, it means we have either exhausted x by divison by 10, or remaining digits are zero that 
        // cannot exist in front of the number and thus not necessary.
        {
            count *= 10;            // Shift all digits of count by 1 to the left
            count += (temp%10);     // Add the last digit of temp to the right
            temp /= 10;             // Modify temp
            // cout<<count<<" ";
        }
        
        // Comparison function
        if(count == x)      
        {return true;}  
        else
        {return false;}
    }
};
