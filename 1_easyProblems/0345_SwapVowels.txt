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
                cout<<"Swapping: "<<s[Start]<<" and "<<s[End]<<"\n";
            }
            Start++;
        }
        return s;
    }
};