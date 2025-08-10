class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:        
        MAX_VALUE = 10**9
        
        def get_digits(number):
            digits = []
            while number > 0:
                digits.append(number%10)
                number //= 10

            return ''.join([str(s) for s in sorted(digits)])

        power_set = set()
        
        i = 0
        while pow(2, i) <= MAX_VALUE:
            sorted_str = get_digits(pow(2, i))
            power_set.add(sorted_str)
            i += 1
        
        return get_digits(n) in power_set
