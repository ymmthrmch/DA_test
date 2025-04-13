import sys
from collections import defaultdict

"""
無向・重み付きの単純グラフ（自己ループ・多重辺なし）が与えられる。
このグラフにおいて、最長の経路を1つ求めて出力する。

- 経路の始点と終点は同じでもよい。
- ただし、同じ頂点を2度以上通ることはできない。
- 同じ辺を2度通ることもできない。
- 頂点のIDは int 型、辺の長さ（重み）は float 型で与えられる。
- 最長経路のうち1つを、改行区切りで出力する。
"""

def main():

    lines = sys.stdin.read().strip().splitlines()

    graph = defaultdict(list)
    distances = {}
    
    for line in lines:
        u, v, d = parse(line)
        graph[u].append(v)
        graph[v].append(u)
        distances[(u, v)] = d
        distances[(v, u)] = d

    ans = [[], float(0)]
    for start in graph.keys():
        dfs(start, set(), [], float(0), ans, graph, distances)

    if len(ans[0]) > 2 and ans[0][0] in graph[ans[0][-1]]:
        ans[0].append(ans[0][0])
        ans[1] += distances.get((ans[0][-2], ans[0][-1]), 0)

    final_ans = "\n".join(str(node) for node in ans[0])

    return final_ans

def dfs(node, visited, path, total_dist, ans, graph, distances):
    visited.add(node)
    path.append(node)

    if ans[1] < total_dist:
        ans[0] = list(path)
        ans[1] = total_dist

    for neighbor in graph[node]:
        if neighbor not in visited:
            dist = distances.get((node, neighbor), 0)
            dfs(neighbor, visited, path, total_dist + dist, ans, graph, distances)

    visited.remove(node)
    path.pop()

def parse(line):
    parts = line.strip().split(",")
    u = int(parts[0].strip())
    v = int(parts[1].strip())
    d = float(parts[2].strip())
    return u, v, d

if __name__ == "__main__":
    print(main())