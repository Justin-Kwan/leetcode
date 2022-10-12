import collections

class Solution:
    # optimal dfs approach
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # build hashmap graph of nodes by adjacency list
        graph = {node: [] for node in range(n)}

        for node, neighborNode in edges:
            # treat each edge adjacency as bidirectional
            graph[node].append(neighborNode)
            graph[neighborNode].append(node)

        # keep track of all nodes visited so far to detect cycle
        visitedNodes = set()
        isCycleFree = self.isCycleFreeGraph(0, -1, visitedNodes, graph)

        # ensure no cycles exists and all nodes are reachable (non-disjoint)
        return isCycleFree and len(visitedNodes) == n

    def isCycleFreeGraph(self, node: int, prevNode: int, visitedNodes: Set[int], graph: Dict[int, int]) -> bool:
        # already visited node means a cycle exists
        if node in visitedNodes:
            return False

        visitedNodes.add(node)

        for neighborNode in graph[node]:
            # avoid incorrectly revisiting and detecting cycle with previous node
            # since all node neighbors have bidirectional adjacency
            if neighborNode == prevNode:
                continue

            if not self.isCycleFreeGraph(neighborNode, node, visitedNodes, graph):
                return False

        return True


#     # optimal bfs approach
#     def validTree(self, n: int, edges: List[List[int]]) -> bool:
#         # build hashmap graph of nodes by adjacency list
#         graph = {node: [] for node in range(n)}

#         for node, neighborNode in edges:
#             # treat each edge adjacency as bidirectional
#             graph[node].append(neighborNode)
#             graph[neighborNode].append(node)

#         # keep track of all nodes visited so far to detect cycle
#         visitedNodes = set()

#         return self.isCycleFreeGraph(visitedNodes, graph) and len(visitedNodes) == n

#     def isCycleFreeGraph(self, visitedNodes: Set[int], graph: Dict[int, int]) -> bool:
#         # each queued node to visit should know it's previous node to avoid
#         nodesToVisit = collections.deque([(-1, 0)])

#         while nodesToVisit:
#             prevNode, curNode = nodesToVisit.popleft()

#             # already visited node means a cycle exists
#             if curNode in visitedNodes:
#                 return False

#             visitedNodes.add(curNode)

#             for neighborNode in graph[curNode]:
#                 # avoid incorrectly revisiting and detecting cycle with previous node
#                 # since all node neighbors have bidirectional adjacency
#                 if neighborNode == prevNode:
#                     continue
#                 nodesToVisit.append((curNode, neighborNode))

#         return True
