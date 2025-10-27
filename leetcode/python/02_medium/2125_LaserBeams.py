class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        prevRow = 0
        totalBeams = 0
        totalRows = len(bank)
        
        for i in range(totalRows):
            currDevices = bank[i].count('1')
            totalBeams += prevRow * currDevices
            if currDevices > 0:
                prevRow = currDevices
            
        return totalBeams
