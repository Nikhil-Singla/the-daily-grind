class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        MOD = 10**9 + 7

        points.sort(key=lambda x: x[1])
        n = len(points)
        valid_y_counts = []
        ongoing_y_count = 1

        for idx in range(n):
            if points[idx][1] == points[idx-1][1]:
                ongoing_y_count += 1
            else:
                if ongoing_y_count >= 2:
                    valid_y_counts.append(ongoing_y_count)

                ongoing_y_count = 1

        if ongoing_y_count >= 2:
            valid_y_counts.append(ongoing_y_count)


        choose_2 = list(map(lambda x: x * (x - 1) // 2 , valid_y_counts))
        total = 0
        n = len(choose_2)

        prefix = 0
        for i in range(n):
            total = (total + (choose_2[i] * prefix)) % MOD
            prefix = (prefix + choose_2[i]) % MOD

        return total % MOD
