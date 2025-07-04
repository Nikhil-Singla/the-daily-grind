class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        n = len(s)
        maxSeqLen = n // k
        freq = [0] * 26

        for i in s:
            freq[ord(i) - ord('a')] += 1

        candidateChar = []
        for idx, i in enumerate(freq):
            if i >= k:
                candidateChar.append(chr(idx+97))

        if not len(candidateChar):
            return ""

        def isSubseq(sub):
            temp = iter(s)
            for c in sub * k:
                if c not in temp:
                    return False

            return True


        # Code proceeding this is DNF, taken from the top solution in leetcode. 
        queue = deque([''])
        result = ''

        while queue:
            for _ in range(len(queue)):
                cur = queue.popleft()
                for c in candidateChar:
                    next_seq = cur + c
                    if isSubseq(next_seq):
                        queue.append(next_seq)
                        if len(next_seq) > len(result) or (len(next_seq) == len(result) and next_seq > result):
                            result = next_seq

        return result
