class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], 
                    containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:

        openedSet = set()       # Set of boxes that have been OPENED
        boxStack = set()        # Set of boxes that we have access to
        answerStack = set()     # Set of boxes which we will use to count candy
        target = set()

        # Below loop finds all opened boxes, and adds them to the opened set.
        for index, state in enumerate(status):
            if state:
                openedSet.add(index)
        
        # Below loop goes through all initial boxes given to use
        # and if boxes are opened, adds to answer stack. If they are
        # have keys, activates their keys, and if they have other boxes
        # adds to the box stack

        for box in initialBoxes:
            if box in openedSet:                    # Check if box is opened
                answerStack.add(box)                # Add the openedbox to candy stack 
                
                for eachBox in containedBoxes[box]: # Check the subboxes present
                    boxStack.add(eachBox)
                
                for eachKey in keys[box]:           # Check keys we get
                    openedSet.add(eachKey)
            else:
                boxStack.add(box)
                
        flag = 0

        # Below loop runs while box stack isn't empty
        while boxStack:
            # Gets a random box from the stack of boxes we have and empties it from the og stack
            currentBox = boxStack.pop()            
            # print("Box: ", boxStack)

            # If the box is already opened, then update our stacks
            if currentBox in openedSet:
                # print("Keys: ", openedSet)
                answerStack.add(currentBox)                 # Add the openedbox to candy stack 
                
                for eachBox in containedBoxes[currentBox]:  # Check the subboxes present
                    boxStack.add(eachBox)
                
                for eachKey in keys[currentBox]:            # Check keys we get
                    openedSet.add(eachKey)
                    
                    # If we get a key of a new box that is in our stack, means we need to 
                    # Run the flag again and check all the boxes.
                    if eachKey in target:
                        flag = 1
            else:
                target.add(currentBox)
                # print("Target: ", target)

            # If box stack is empty, and we had at least one update, then we need to recheck 
            # Each box in the stack for updates.

            if (not boxStack) and flag:
                # If there were updates, then we need to rerun the OG stack, otherwise we will exit.
                boxStack.update(target)
                target = set()
                # Resets the update.
                flag = 0

        retVal = 0
        # print("Answer: ", answerStack)

        for answer in answerStack:
            retVal += candies[answer]

        return retVal            