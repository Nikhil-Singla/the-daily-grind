# Weekly Contest 459
# Q1 Easy: Code passing all testcases
class Solution:
    def checkDivisibility(self, n: int) -> bool:
        digits = []
        temp = n
        while temp > 0:
            digits.append(int(temp%10))
            temp = int(temp / 10)
        prod = 1
        for x in digits:
            prod *= x    
            
        sumD = sum(digits)
        return (n % (sumD+prod) == 0)
    
# Q2 Medium: Code passing all testcases
class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        MOD = 10**9 + 7
        inv2 = (MOD + 1) // 2    # modular inverse of 2

        def choose2(num):
            return int((num * (num-1)) / 2)
        
        buckets = defaultdict(int)
        YCOORDINATE = 1
        
        for onePoint in points:
            buckets[onePoint[YCOORDINATE]] += 1

        finalList = []
        for indices, count in buckets.items():
            if count >= 2:
                finalList.append(choose2(count))

        sumL = sum(finalList)
        
        retVal = 0
        for i in finalList:
            retVal += (sumL - i) * i
            retVal %= MOD

        # Need to divide as I am returning pairs of both A,B and B,A
        return retVal * inv2 % MOD
    
# Q4 Hard: 432/550 Testcases passed. Possible error: Parallelograms causing double counting.
class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        buckets = defaultdict(int)
        points.sort()
        print(points)
        def getSlope(point1, point2):
            mx = point2[0] - point1[0]
            my = point2[1] - point1[1]
            if mx == 0:
                slope = None
            else:
                slope = my/mx
                
            if slope is None:
                intercept = point2[0]
            else:
                intercept = point1[1] - (slope * point1[0])
            
            return slope, intercept

        sumLines = 0
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                angle, intersect = getSlope(points[i], points[j])     
                buckets[(angle, intersect)] += 1
                sumLines += 1
                        
        slopeSum = defaultdict(int)
        for (angle, intersect), count in buckets.items():
            slopeSum[angle] += count
            # We now need to create buckets of similar sloped lines
        
        retVal = 0
        for (angle, intersect), count in buckets.items():
            otherParallelLines = slopeSum[angle] - count
            retVal += otherParallelLines * count

        # In every pair A,B is counted twice, so we now divide by 2
        return retVal // 2
        

# Q3 Hard: DNF. Solution by "Oh a clown"

class SegmentTree:
    def __init__(self, nums):
        self.n = len(nums)
        self.tree = [[0] * 6 for _ in range(self.n * 4)]
        self.build(0, self.n - 1, 1, nums)

    def build(self, left, right, node, nums):
        if left == right:
            depth = self.get_depth(nums[left])
            self.tree[node][depth] = 1
            return
        mid = left + (right - left) // 2
        self.build(left, mid, node * 2, nums)
        self.build(mid + 1, right, node * 2 + 1, nums)
        for i in range(6):
            self.tree[node][i] = self.tree[node * 2][i] + self.tree[node * 2 + 1][i]

    def update(self, index, val, left, right, node):
        if left == right:
            self.tree[node] = [0] * 6
            new_depth = self.get_depth(val)
            self.tree[node][new_depth] = 1
            return
        mid = left + (right - left) // 2
        if index <= mid:
            self.update(index, val, left, mid, node * 2)
        else:
            self.update(index, val, mid + 1, right, node * 2 + 1)
        for i in range(6):
            self.tree[node][i] = self.tree[node * 2][i] + self.tree[node * 2 + 1][i]

    def get_number(self, left, right, tleft, tright, node, k):
        if right < tleft or left > tright:
            return 0

        if left <= tleft and tright <= right:
            return self.tree[node][k]

        mid = tleft + (tright - tleft) // 2
        return self.get_number(left, right, tleft, mid, node * 2, k) + self.get_number(left, right, mid + 1, tright, node * 2 + 1, k)

    @cache
    def get_depth(self, i):
        d = 0
        while i > 1:
            i = bin(i).count('1')
            d += 1
        return d

class Solution:
    def popcountDepth(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        tree = SegmentTree(nums)
        res = []
        for q in queries:
            if q[0] == 1:
                _, l, r, k = q
                res.append(tree.get_number(l, r, 0, tree.n - 1, 1, k))
            else:
                _, idx, val = q
                tree.update(idx, val, 0, tree.n - 1, 1)
        return res               

