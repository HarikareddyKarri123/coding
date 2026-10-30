from typing import List
import heapq

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        graph = [[] for _ in range(n)]

        for u, v, w in edges:
            graph[u].append((v, w))

        # dist[node][run] stores minimum cost for that state
        dist = [[float('inf')] * (k + 1) for _ in range(n)]

        dist[0][1] = 0
        pq = [(0, 0, 1)]

        while pq:
            cost, node, run = heapq.heappop(pq)

            if cost != dist[node][run]:
                continue

            if node == n - 1:
                return cost

            for nxt, weight in graph[node]:
                if labels[nxt] == labels[node]:
                    new_run = run + 1
                else:
                    new_run = 1

                if new_run > k:
                    continue

                new_cost = cost + weight

                if new_cost < dist[nxt][new_run]:
                    dist[nxt][new_run] = new_cost
                    heapq.heappush(pq, (new_cost, nxt, new_run))

        return -1