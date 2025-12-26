class Solution:
    def bestClosingTime(self, customers: str) -> int:

        incoming = customers.count('Y')
        high_score = float('-inf')
        curr_score = 0
        index = 0

        for idx, i in enumerate(customers):
            if i == 'Y':
                # We can keep updating as it only tracks at the end
                # print("One Iter:", incoming, curr_score, high_score, index)
                incoming -= 1
            else:
                # print("One Iter:", incoming, curr_score, high_score, index)

                if curr_score-incoming > high_score:
                    high_score = curr_score - incoming
                    index = idx
                
                curr_score -= 1

        # print("Final Iter:", incoming, curr_score, high_score, index)

        if curr_score-incoming > high_score:
            return len(customers)

        return index
