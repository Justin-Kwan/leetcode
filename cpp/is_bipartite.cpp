class Solution {
public:
    // optimal bfs approach
    bool isBipartite(vector<vector<int>> &graph) {
        // track the distance between start node to each reachable vertex
        vector<int> distances(graph.size(), INT_MAX);

        // launch bfs from every single node to handle disconnected components
        for (int node = 0; node < graph.size(); ++node) {
            countDistances(graph, distances, node);
        }

        // examine two nodes incident to every edge
        for (int node = 0; node < graph.size(); ++node) {
            for (int neighbor : graph[node]) {
                // odd cycle exists if both nodes are odd or even distance away from start node
                if (distances[node] % 2 == distances[neighbor] % 2) {
                    return false;
                }
            }
        }

        return true;
    }

    void countDistances(vector<vector<int>> &graph, vector<int> &distances, int startNode) {
        // start node already visited from previous bfs within same component
        if (distances[startNode] != INT_MAX) {
            return;
        }

        // mark starting node of component as visited
        distances[startNode] = 0;
        queue<int> nodesToVisit({ startNode });

        while (!nodesToVisit.empty()) {
            int curNode = nodesToVisit.front();
            nodesToVisit.pop();

            for (int neighbor : graph[curNode]) {
                if (distances[neighbor] == INT_MAX) {
                    // compute shortest distance for neighbor node using current's distance
                    distances[neighbor] = distances[curNode] + 1;
                    nodesToVisit.push(neighbor);
                }
            }
        }
    }
};
