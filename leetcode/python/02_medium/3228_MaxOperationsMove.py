class Solution:
    def maxOperations(self, input_string: str) -> int:
        count_of_ones = 0
        final_count = 0
        can_do_operation = False

        for an_element in input_string:
            if an_element == '1':
                if can_do_operation:
                    can_do_operation = False
                    final_count += count_of_ones

                count_of_ones += 1

            elif an_element == '0':
                can_do_operation = True

        if can_do_operation == True:
            final_count += count_of_ones

        return final_count
