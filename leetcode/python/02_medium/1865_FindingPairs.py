class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums2 = nums2
        self.dictOfnums1 = Counter(nums1)
        self.dictOfnums2 = Counter(nums2)
        self.nums1Key = sorted(self.dictOfnums1.keys())

    def add(self, index: int, val: int) -> None:
        self.dictOfnums2[self.nums2[index]] -= 1

        self.nums2[index] += val

        self.dictOfnums2[self.nums2[index]] += 1


    def count(self, tot: int) -> int:
        retVal = 0
        for i in self.nums1Key:
            if i >= tot:
                break
            
            if tot-i in self.dictOfnums2:
                retVal += self.dictOfnums2[tot-i] * self.dictOfnums1[i]

        return retVal


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)