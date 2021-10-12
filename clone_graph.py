"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    # dfs
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is None:
            return None
        cloneHead = Node()
        self.dfsClone(node, cloneHead, {})
        return cloneHead

    def dfsClone(self, node: 'Node', cloneNode: 'Node', visitedNodes):
        cloneNode.val = node.val
        visitedNodes[node.val] = cloneNode
        for i in range( len(node.neighbors) ):
            if node.neighbors[i].val not in visitedNodes: # if node not seen yet
                cloneChild = Node()                     # create child node clone
                cloneNode.neighbors.append(cloneChild) # connect it to current clone
                visitedNodes = self.dfsClone(node.neighbors[i], cloneChild, visitedNodes)
            else:   # if node has been seen
                # get seen node from hashmap and connect it to current clone
                visitedNode = visitedNodes[node.neighbors[i].val]
                cloneNode.neighbors.append(visitedNode)
        return visitedNodes

#     # bfs
#     def cloneGraph(self, node: 'Node') -> 'Node':
#         if node is None:
#             return None
#         cloneHead = Node()
#         nodeQueue = [node]
#         createdNodes = {node.val: cloneHead} # put first clone in map
        
#         while nodeQueue:
#             refNode = nodeQueue.pop(0)
#             cloneNode = createdNodes[refNode.val] # get blank clone node from map
#             cloneNode.val = refNode.val           # copy value to clone node
#             for i in range(len(refNode.neighbors)):
#                 # if neighbor is already created (either in queue or completed)
#                 if refNode.neighbors[i].val in createdNodes:
#                     createdAlreadyNeighbor = createdNodes[refNode.neighbors[i].val]
#                     cloneNode.neighbors.append(createdAlreadyNeighbor)
#                 else:
#                     cloneChild = Node()
#                     nodeQueue.append(refNode.neighbors[i])
#                     cloneNode.neighbors.append(cloneChild)
#                     # add to hashmap of created nodes
#                     createdNodes[refNode.neighbors[i].val] = cloneChild
#         return cloneHead

