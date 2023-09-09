class Solution:
    # union find with path compression
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # assume each node is disjoint component so the parent of each node should
        # be itself initially
        nodeParents = list(range(n))
        componentCount = n

        # for each edge pair of nodes merged, number of components reduces by one
        for startNode, endNode in edges:
            isCombined = self.union(startNode, endNode, nodeParents)
            # do not account for two nodes already in same component (ex. cycle)
            if isCombined:
                componentCount -= 1

        return componentCount

    def union(self, startNode: int, endNode: int, nodeParents: List[int]) -> bool:
        startRoot = self.findRoot(startNode, nodeParents)
        endRoot = self.findRoot(endNode, nodeParents)

        # skip merging if both nodes are already in same component
        if startRoot == endRoot:
            return False

        # attach end node's root to start node's root to merge both
        nodeParents[endRoot] = startRoot
        return True

    def findRoot(self, node: int, nodeParents: List[int]) -> int:
        # each component's root should be the parent of itself
        if node == nodeParents[node]:
            return node

        # since current node has a parent above in the path, find the root and
        # update it as the parent of the current node to compress the path and
        # reduce future root lookup recursive calls
        root = self.findRoot(nodeParents[node], nodeParents)
        nodeParents[node] = root
        return root

    # # optimal build graph dfs
    # def countComponents(self, n: int, edges: List[List[int]]) -> int:
    #     graph, visited = defaultdict(list), set()
    #     componentCount = 0

    #     # construct hashmap graph of nodes to adjacency lists, graph may
    #     # not be directed in increasing node order so add reverse link
    #     for startNode, endNode in edges:
    #         graph[startNode].append(endNode)
    #         graph[endNode].append(startNode)

    #     # search each component starting from arbitrary node in graph,
    #     # not necessarily first
    #     for node in range(n):
    #         if node not in visited:
    #             self.searchComponent(node, graph, visited)
    #             componentCount += 1

    #     return componentCount

    # def searchComponent(self, node: int, graph: dict[int, List[int]], visited: set[int]):
    #     # reached a node already visited
    #     if node in visited:
    #         return

    #     visited.add(node)
    #     # exit if current node is a leaf in the component
    #     if node not in graph:
    #         return

    #     for neighborNode in graph[node]:
    #         self.searchComponent(neighborNode, graph, visited)
