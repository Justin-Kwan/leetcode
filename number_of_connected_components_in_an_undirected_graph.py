class Solution:
    # optimal build graph dfs
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph, visited = defaultdict(list), set()
        componentCount = 0

        # construct hashmap graph of nodes to adjacency lists, graph may
        # not be directed in increasing node order so add reverse link
        for startNode, endNode in edges:
            graph[startNode].append(endNode)
            graph[endNode].append(startNode)

        # search each component starting from arbitrary node in graph,
        # not necessarily first
        for node in range(n):
            if node not in visited:
                self.searchComponent(node, graph, visited)
                componentCount += 1

        return componentCount

    def searchComponent(self, node: int, graph: Dict[int, List[int]], visited: Set[int]):
        # reached a node already visited
        if node in visited:
            return

        visited.add(node)
        # exit if current node is a leaf in the component
        if node not in graph:
            return

        for neighborNode in graph[node]:
            self.searchComponent(neighborNode, graph, visited)
