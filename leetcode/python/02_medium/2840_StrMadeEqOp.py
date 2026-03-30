class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        def get_strs(input_string):
            is_odd_flag = True
            evens = []
            odds = []

            for i in input_string:
                if is_odd_flag:
                    odds.append(i)
                else:
                    evens.append(i)
                
                is_odd_flag = not is_odd_flag
            
            return sorted(evens), sorted(odds)

        a, b = get_strs(s1)
        c, d = get_strs(s2)

        return (a==c) and (b==d)
