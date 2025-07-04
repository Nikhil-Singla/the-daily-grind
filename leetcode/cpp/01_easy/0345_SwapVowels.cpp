// Compacted version of the code
class Solution {
public:

    bool iV(char c)     // is Vowel function
    {
        char d = tolower(c);
        return ( d=='a' || d=='e' || d=='i' || d=='o' || d=='u' );
    }

    string reverseVowels(string s) 
    {
        int start = 0, end = s.length()-1;
        while(start < end)
        {
            while(start < end && !iV(s[start])) start++;
            while(start < end && !iV(s[end])) end--;
            swap(s[start],s[end]);
            start++;end--;
        }
        return s;
    }
};

// Initial, unrefined version of the code
class Solution {
public:

    bool iV(char c)     // is Vowel function
    {
        char d = tolower(c);
        return ( d=='a' || d=='e' || d=='i' || d=='o' || d=='u' );
    }

    string reverseVowels(string s) 
    {
        int Start = 0, End = s.length()-1;
        bool flag;
        while(Start < End)
        {
            if( iV(s[Start]) )
            {
                while( (!iV(s[End])) && (Start < End) )
                {
                    End--;
                }
                if(iV(s[End]) && Start != End) { swap( s[Start], s[End--] ); }
            }
            Start++;
        }
        return s;
    }
};
