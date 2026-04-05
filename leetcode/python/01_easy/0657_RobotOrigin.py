class Solution:
    def judgeCircle(self, moves: str) -> bool:
        return moves.count('U')==moves.count('D') and moves.count('L')==moves.count('R')


'''
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        horizon = 0
        vert = 0

        for i in moves:
            match i:
                case 'L':
                    horizon -= 1
                case 'R':
                    horizon += 1
                case 'U':
                    vert += 1
                case 'D':
                    vert -=1 
        
        return horizon == vert == 0
'''
