# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """

        if not root: return "null"

        retVal, frontLine = [], deque([root])

        while frontLine:
            node = frontLine.popleft()
            if node:
                retVal.append(str(node.val))
                frontLine.append(node.left)
                frontLine.append(node.right)
            else:
                retVal.append("null") 

        return ','.join(retVal)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """

        treeList = data.split(',')
        retVal = deque()

        if treeList is None:
            return []

        for i in treeList:
            if i == "null":
                retVal.append(None)
            else:
                retVal.append(int(i))

        if retVal[0] is None:
            return []

        root = TreeNode(retVal[0])
        retVal.popleft()
        frontLine = deque([root])

        while frontLine:
            node = frontLine.popleft()

            if node is None:
                continue

            if retVal is not None:
                tempVal = retVal.popleft()
                if tempVal is not None:
                    child1 = TreeNode(tempVal)
                    frontLine.append(child1)
                else:
                    child1 = None
            else:
                child1 = None

            node.left = child1

            if retVal is not None:
                tempVal = retVal.popleft()
                if tempVal is not None:
                    child2 = TreeNode(tempVal)
                    frontLine.append(child2)
                else:
                    child2 = None
            else:
                child2 = None

            node.right = child2

        return root

        # for i in retVal[::-1]:
        #     if i is None:
        #         count += 1
        #     else:
        #         break

        # retVal = retVal[:-count:]


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
