# [A1] [SO] [M.CHECK]

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1 = version1.split('.')
        version2 = version2.split('.')

        while len(version1) < len(version2):
            version1.append(0)
        
        while len(version2) < len(version1):
            version2.append(0)

        for i, j in zip(version1, version2):
            if int(i) > int(j):
                return 1
            
            if int(i) < int(j):
                return -1

        return 0
