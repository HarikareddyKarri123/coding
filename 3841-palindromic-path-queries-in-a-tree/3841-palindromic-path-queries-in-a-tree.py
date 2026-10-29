from typing import List
import sys

class Solution:
    def palindromePath(self, n: int, edges: List[List[int]], s: str, queries: List[str]) -> List[bool]:
        sys.setrecursionlimit(1_000_000)

        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        parent = [0] * n
        depth = [0] * n
        tin = [0] * n
        tout = [0] * n
        prefix = [0] * n
        timer = 0

        # Iterative DFS to avoid recursion-depth problems
        stack = [(0, -1, 0)]

        while stack:
            u, p, state = stack.pop()

            if state == 0:
                parent[u] = u if p == -1 else p
                tin[u] = timer
                timer += 1

                prefix[u] = (0 if p == -1 else prefix[p]) ^ (1 << (ord(s[u]) - ord('a')))

                stack.append((u, p, 1))

                for v in reversed(graph[u]):
                    if v != p:
                        depth[v] = depth[u] + 1
                        stack.append((v, u, 0))
            else:
                tout[u] = timer - 1

        # Binary lifting table for LCA
        LOG = n.bit_length()
        up = [parent[:]]

        for j in range(1, LOG):
            prev = up[j - 1]
            up.append([prev[prev[i]] for i in range(n)])

        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u

            diff = depth[u] - depth[v]
            for j in range(LOG):
                if diff & (1 << j):
                    u = up[j][u]

            if u == v:
                return u

            for j in range(LOG - 1, -1, -1):
                if up[j][u] != up[j][v]:
                    u = up[j][u]
                    v = up[j][v]

            return parent[u]

        # Fenwick tree supporting range XOR updates
        bit = [0] * (n + 2)

        def update(i, value):
            i += 1
            while i < len(bit):
                bit[i] ^= value
                i += i & -i

        def query_prefix(i):
            i += 1
            value = 0
            while i > 0:
                value ^= bit[i]
                i -= i & -i
            return value

        def range_update(left, right, value):
            update(left, value)
            if right + 1 < n:
                update(right + 1, value)

        # Required intermediate input variable
        suneravilo = (n, edges, s, queries)

        chars = list(s)
        answer = []

        for q in queries:
            parts = q.split()

            if parts[0] == "update":
                u = int(parts[1])
                c = parts[2]

                old_mask = 1 << (ord(chars[u]) - ord('a'))
                new_mask = 1 << (ord(c) - ord('a'))
                delta = old_mask ^ new_mask

                if delta:
                    range_update(tin[u], tout[u], delta)
                    chars[u] = c

            else:
                u = int(parts[1])
                v = int(parts[2])
                w = lca(u, v)

                pu = prefix[u] ^ query_prefix(tin[u])
                pv = prefix[v] ^ query_prefix(tin[v])
                w_mask = 1 << (ord(chars[w]) - ord('a'))

                path_mask = pu ^ pv ^ w_mask

                # At most one character may have an odd frequency
                answer.append((path_mask & (path_mask - 1)) == 0)

        return answer