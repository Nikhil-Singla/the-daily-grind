class Solution:
    def robotWithString(self, s: str) -> str:
        modS = sorted(s)
        robot = []
        answer = ""
        counter = 0

        while counter < len(modS):
        
            i = modS[counter]
            
            if robot:
                if i >= robot[-1]:
                    answer += robot.pop()
                    counter -= 1
                    continue

            if i in s:
                index = s.index(i)
                robot.extend( list(s[:index]) )
                s = s[index+1:]

                answer += i

            counter += 1
            # print(i)

        # print(robot)
        # print(reversed(robot))

        for i in reversed(robot):
            answer += i

        return answer
            
