class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:

        if k == 1:
            return 'a'

        count = 1

        reverse = []
        shift = 0

        for idx, i in enumerate(operations):
            # print(idx, i, count)

            if count >= k:
                reverse = operations[:idx]
                # print(reverse)
                break

            count *= 2

        if not reverse:
            reverse = operations[::-1]
        else:
            reverse = reverse[::-1]

        for i in reverse:
            # print(i, count, k)
            count //= 2

            if i:
                if k > count:
                    shift += 1
                    k -= (count)
                    
                    # print(k)

            else:

                if k > count:
                    k -= (count)

        return chr((shift % 26) + ord('a'))
