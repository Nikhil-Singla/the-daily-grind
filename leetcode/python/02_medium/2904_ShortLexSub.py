class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        if k == 1:
            return ('1' if '1' in s else "")

        start = s.find('1')
        if start < 0:   # Does the string contain any 1's?
            return ""

        n = len(s)


        s = s[start:]   # Trimming the first excess 0's to shorten
        diff = []       # The array of counts between different, consecutive 1's
        csp = 0         # count_since_previous `1` has occured

        for i in s[1:]:
            if i == '1':
                diff.append(csp)
                csp = 0
            else:
                csp += 1

        # note how we didn't do a final append of csp after the loop ends.
        # thats because we throw away the last element if its not a 1,
        # because we only need to get the digits enclosed by 1
        # for shortest substring.

        if len(diff) + 1 < k:   # Not enough 1's to form a beautiful substring
            return ""

        window = k-1    # The elements of the array are akin to a bounded box. The first element represents
                        # the edges of the window, ie 2 1's. Every additional element just adds another 1
                        # This means

        cs = 0          # value of currentely selected string
        ms = n+1        # minimum selected string by value (also lexicographically smallest)
        array = []
        for i in range(0, len(diff) - window + 1, 1):            
            current_diff = diff[i:i + window]
            cs = sum(current_diff)

            if cs < ms:
                ms = cs
                array = current_diff
            elif cs == ms and current_diff > array:
                array = current_diff

        ans = ['1']
        for i in array:
            ans.extend(['0']*i + ['1'])

        return "".join(ans)
