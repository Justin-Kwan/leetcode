class Solution {
public:
    int networkDelayTime(vector<vector<int>>& times, int n, int k) {
        // create directed graph from list of edges and weights
        vector<vector<pair<int, int>>> graph(n, vector<pair<int, int>>({}));
        for (auto &edge : times) {
            int node = edge[0] - 1;
            int neighbor = edge[1] - 1;
            int latency = edge[2];
            graph[node].push_back({ latency, neighbor });
        }

        // find the fastest low latency (SSSP) paths from source to every other node
        vector<int> latencies(graph.size(), INT_MAX);
        findFastestPaths(graph, latencies, k - 1);

        // path with latency of infinity was not reachable (no path)
        int maxPathLatency = *max_element(begin(latencies), end(latencies));
        return maxPathLatency == INT_MAX ? -1 : maxPathLatency;
    }

    // optimal bfs dijkstra approach
    void findFastestPaths(vector<vector<pair<int, int>>> &graph, vector<int> &latencies, int startNode) {
        set<pair<int, int>> nodesToVisit({{0, startNode}});
        latencies[startNode] = 0;

        // each vertex has one entry in priority queue, start node has smallest cost
        for (int node = 1; node < graph.size(); ++node) {
            nodesToVisit.insert({ latencies[node], node });
        }

        while (!nodesToVisit.empty()) {
            int curNode = nodesToVisit.begin()->second;
            nodesToVisit.erase(nodesToVisit.begin());

            for (auto &[weight, neighbor] : graph[curNode]) {
                if (latencies[curNode] < INT_MAX && latencies[curNode] + weight < latencies[neighbor]) {
                    // updating priority of already queued (relaxed) neighbor that is GRAY
                    nodesToVisit.erase({ latencies[neighbor], neighbor });
                    latencies[neighbor] = latencies[curNode] + weight;
                    nodesToVisit.insert({ latencies[neighbor], neighbor });
                }
            }
        }
    }

    // // optimal bfs dijkstra variant approach
    // void findFastestPaths(vector<vector<pair<int, int>>> &graph, vector<int> &latencies, int startNode) {
    //     priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> nodesToVisit;

    //     nodesToVisit.push({ 0, startNode });
    //     latencies[startNode] = 0;

    //     while (!nodesToVisit.empty()) {
    //         int curNode = nodesToVisit.top().second;
    //         nodesToVisit.pop();

    //         // edge relaxation of neighbors
    //         for (auto &[weight, neighbor] : graph[curNode]) {
    //             if (latencies[curNode] + weight < latencies[neighbor]) {
    //                 latencies[neighbor] = latencies[curNode] + weight;
    //                 // queueing queued (relaxed) neighbor that is GRAY potentially again
    //                 nodesToVisit.push({ latencies[neighbor], neighbor });
    //             }
    //         }
    //     }
    // }

    // // bfs spfa approach (https://en.wikipedia.org/wiki/Shortest_path_faster_algorithm)
    // void findFastestPaths(vector<vector<pair<int, int>>> &graph, vector<int> &latencies, int startNode) {
    //     queue<int> nodesToVisit({ startNode });
    //     vector<bool> isNodeQueued(graph.size(), false);

    //     latencies[startNode] = 0;
    //     isNodeQueued[startNode] = true;

    //     while (!nodesToVisit.empty()) {
    //         int curNode = nodesToVisit.front();
    //         nodesToVisit.pop();
    //         isNodeQueued[curNode] = false;

    //         // edge relaxation of neighbors
    //         for (auto &[weight, neighbor] : graph[curNode]) {
    //             if (latencies[curNode] + weight < latencies[neighbor]) {
    //                 latencies[neighbor] = latencies[curNode] + weight;
    //                 // queueing queued (relaxed) neighbor that is GRAY potentially again

    //                 if (!isNodeQueued[neighbor]) {
    //                     nodesToVisit.push(neighbor);
    //                     isNodeQueued[neighbor] = true;
    //                 }
    //             }
    //         }
    //     }
    // }

    // // bfs bellman ford approach
    // void findFastestPaths(vector<vector<pair<int, int>>> &graph, vector<int> &latencies, int startNode) {
    //     latencies[startNode] = 0;

    //     for (int _ = 0; _ < graph.size(); ++_) {
    //         bool isUpdated = false;

    //         for (int node = 0; node < graph.size(); ++node) {
    //             for (auto &[nextWeight, neighbor] : graph[node]) {
    //                 if (latencies[node] < INT_MAX && latencies[node] + nextWeight < latencies[neighbor]) {
    //                     latencies[neighbor] = latencies[node] + nextWeight;
    //                     isUpdated = true;
    //                 }
    //             }
    //         }

    //         if (!isUpdated) {
    //             break;
    //         }
    //     }
    // }
};
