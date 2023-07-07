# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# bfs encoding approach
class Codec:
    def serialize(self, root: TreeNode) -> str:
        encodedTree = ""
        nodesToVisit = collections.deque([root])

        while nodesToVisit:
            # add current parent node to encoded string
            curNode = nodesToVisit.popleft()
            encodedTree += "N" if not curNode else str(curNode.val)

            # queue next layer children of current node to be encoded later
            if curNode:
                nodesToVisit.append(curNode.left)
                nodesToVisit.append(curNode.right)

            # only add comma if more nodes will be visited after adding
            # children, must check after adding children since queue could
            # have been temporarily empty after popping first node
            if nodesToVisit:
                encodedTree += ","

        return encodedTree

    def deserialize(self, data: str) -> TreeNode:
        if data == "N":
            return None

        nodeValues , curNodePos = data.split(","), 0
        root = TreeNode(nodeValues[0])
        nodesToVisit = collections.deque([root])

        while nodesToVisit and curNodePos < len(nodeValues) - 1:
            # look-ahead and construct children of current node to check
            # whether they exist or are null rather than pre-emptively
            # constructing children that may be null
            curNode = nodesToVisit.popleft()

            # construct and add children to current node, then queue them
            # to construct their children later (skipping null children)
            if nodeValues[curNodePos + 1] != "N":
                curNode.left = TreeNode(nodeValues[curNodePos + 1])
                nodesToVisit.append(curNode.left)
            if nodeValues[curNodePos + 2] != "N":
                curNode.right = TreeNode(nodeValues[curNodePos + 2])
                nodesToVisit.append(curNode.right)

            # point right before left child of next node in queue
            curNodePos += 2

        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
