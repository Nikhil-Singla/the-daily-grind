class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        number_of_columns = len(strs[0])
        highest_alphabet = [*strs[0]]
        count = [False] * number_of_columns

        for i in strs[1:]:
            current_alphabet = [*i]
            for cur_column in range(number_of_columns):
                if highest_alphabet[cur_column] > current_alphabet[cur_column]:
                    count[cur_column] = True

                highest_alphabet[cur_column] = current_alphabet[cur_column]

        return sum(count)
