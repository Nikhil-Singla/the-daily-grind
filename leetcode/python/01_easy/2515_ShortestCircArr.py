class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        if words[startIndex] == target:
            return 0
        
        n = len(words)
        iterateafter = (startIndex + 1) % n
        iteratebefore = (startIndex - 1 + n) % n

        elements = [-1, -1]

        steps = 1
        while iteratebefore != startIndex and words[iteratebefore] != target:
            iteratebefore = (iteratebefore + n - 1) % n
            steps += 1

        if iteratebefore != startIndex:
            elements[0] = steps

        steps = 1
        while iterateafter != startIndex and words[iterateafter] != target:
            iterateafter = (iterateafter + 1) % n
            steps += 1

        if iterateafter != startIndex:
            elements[1] = steps

        return min(elements)
