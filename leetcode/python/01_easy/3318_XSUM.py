class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        ELEMENT_LIMIT = x
        WINDOW = k

        def get_xsum(inputArray):
            countedElements = Counter(inputArray)
            pairs = [(element,frequency) for element,frequency in countedElements.items()] 
            # print("Unsorted counts: ", pairs)
            pairs.sort(key=lambda items: (items[1], items[0]), reverse=True)
            summation = 0
            # print("Sorted counts: ", pairs)
            for ele, freq in pairs[:ELEMENT_LIMIT]:
                summation += ele*freq

            # print("XSUM: ", summation)
            return summation
        
        iterations = len(nums) - k + 1
        answer = [0] * iterations
        for i in range(iterations):
            # print(nums[i:i+WINDOW])
            answer[i] = get_xsum(nums[i:i+WINDOW])

        return answer
