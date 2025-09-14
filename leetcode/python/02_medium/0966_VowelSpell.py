# [A1] [SO] [M.CHECK] Speed focused code with memory usage
class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        # Declare the alt character to be used (must be reserve character)
        # We also create string of vowels (learnt fastest method from previous leetcode exercise)
        vowels = "aeiou"
        alt_char = '*'

        def remove_vowels(input_word, alt_char='*'):
            temp = input_word.lower()
            for one_vowel in vowels:
                temp = temp.replace(one_vowel, alt_char)

            return temp

        # A dict mapping of original word to lowercase form
        lower_word = {}
        for i in wordlist: 
            if i.lower() not in lower_word:
                lower_word[i.lower()] = i

        # Convert wordlist to set of wordlists for faster lookup 
        wordlist = set(wordlist)

        vowel_error = {}
        for i in lower_word.values():
            temp = remove_vowels(i, alt_char)                
            # print(temp)
            if temp not in vowel_error:
                vowel_error[temp] = lower_word[i.lower()]

        ans = []
        for i in queries:
            if i in wordlist:
                ans.append(i)
                continue

            i = i.lower()
            if i in lower_word:
                ans.append(lower_word[i])
                continue

            a = remove_vowels(i)
            if a in vowel_error:
                ans.append(vowel_error[a])
            else:
                ans.append("")

        return ans
