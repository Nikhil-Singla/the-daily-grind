class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        count = 1        
        tracker = 0

        while tracker <= n:
            if count <= n:
                tracker += 1

            if tracker == k:
                return count

            if count*10 <= n:
                count *= 10
            else:
                while count > n or count%10 == 9:
                    count = count // 10
                
                count += 1

        return 0
                