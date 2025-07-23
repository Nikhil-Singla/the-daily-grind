class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        if x > y:   # If the ab is scored higher, then we need to prioritize it.
            firstString, firstScore = "ab", x
            secondString, secondScore = "ba", y
        else:       # Otherwise prioritize ba and its scoring.
            firstString, firstScore = "ba", y
            secondString, secondScore = "ab", x

        stack = [""] * len(s)   # Init a stack to the max length of the input
        score = 0               # Starting score is 0
        stackPointer = 0        # Stack pointer starts by pointing at the top of the stack (0th index)

        for i in s:                         # For each letter in the input
            
            if stackPointer == 0:           # If our stack is empty
                stack[stackPointer] = i     # Set the top of the stack to be the current letter
                stackPointer += 1           # Move the stack pointer up to a new space that is "empty" (technically)
                continue                    # Go to next iteration as stack has just been initialized

            # If the second element of our priority matches, test for the first element matching in the first occupied stack location
            if i == firstString[1] and stack[stackPointer-1] == firstString[0]:     
                score += firstScore     # If both the prio elements match, that means the string can be directly scored. 
                stackPointer -= 1       # Counts as popping the last element. Since we didn't input the current element, equivalent to push and then popping twice to score.
            else:
                stack[stackPointer] = i # If the prio elements don't match, simply write to stack and go to the next "empty" location in stack
                stackPointer += 1

        count_1 = 0     # Init count of the second prio element. But the first letter only

        for i in stack[:stackPointer]:  # Only the stack is used now as it is the reduced form with letters removed that have been scored.
            if i == secondString[0]:    # To do it in one pass, we just check if the current letter is in our starting prio
                count_1 += 1            # If it is, we add 1 to its count

            elif i == secondString[1] and count_1 > 0:  # If the current is our second letter in prio word, we need to check what our ongoing count is for the first letter of prio word.
                count_1 -= 1                            # This will only run if it exists, hence we can pair up one of the alphabets with the current i. And add to score and remove from count
                score += secondScore
            else:                       # Else Case, triggers when the letters don't match. Sort of a wall that cannot be moved or replaced
                count_1 = 0             # Resetting count because of the wall interfering, and hence we need to reset our tracker.

        return score    # Return the final score of the two phrases combined.