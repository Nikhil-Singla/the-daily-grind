class Solution:
    def numSub(self, s: str) -> int:
        # Let there be a continous string of only 1's of length n
        # Start i at 0. Then j can be put at any number from 0 - n to form a valid
        # substring. Similarly, then move i to 1, and you can do the same for 1-n
        # In this way, for the first element, we have n valid substrings. Then we have
        # n-1 valid subs... so for a string of length n of all 1's, our valid substrings
        # become n + n-1 + n-2 + n-3...+1 and it is inclusive (You can verify)

        # The sum of first n numbers then becomes n*n+1 // 2
        # So for a string of all 1's of length n, we know valid substrings. 
        # Now we just calculate how many strings of all 1's we have, and what's their length.

        ongoing_count = 0
        total_subarrays = 0
        RESET = 0
        MOD = (10**9+7)

        def valid_substrings_for_(input_number):
            return (input_number * (input_number+1)) // 2

        for i in s:
            if i == '1':
                ongoing_count += 1

            if i == '0':
                total_subarrays += valid_substrings_for_(ongoing_count)
                ongoing_count = RESET

        if ongoing_count:
            total_subarrays += valid_substrings_for_(ongoing_count)

        return total_subarrays % MOD
