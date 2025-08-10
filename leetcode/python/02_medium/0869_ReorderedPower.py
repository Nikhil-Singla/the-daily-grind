class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:        
        MAX_VALUE = 10**9
        
        def get_digits(number):
            return ''.join(sorted(str(number)))

        power_set = set()
        
        i = 0
        while pow(2, i) <= MAX_VALUE:
            sorted_str = get_digits(pow(2, i))
            power_set.add(sorted_str)
            i += 1
        
        return get_digits(n) in power_set
