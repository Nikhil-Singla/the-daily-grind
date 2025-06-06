class Solution:
    def robotWithString(self, s: str) -> str:
        modS = sorted(s)
        robot = []
        answer = ""
        for i in modS:
            if robot:
                if i == robot[-1]:
                    answer += robot.pop()
                    continue

            if i in s:
                index = s.index(i)
                robot.extend( list(s[:index]) )
                s = s[index+1:]

                answer += i
            # print(i)

        # print(robot)
        # print(reversed(robot))

        for i in reversed(robot):
            answer += i

        return answer
            
