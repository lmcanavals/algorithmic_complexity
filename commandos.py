import graph_algorithms as ga

T = int(input().strip())

for case in range(T):
  N = int(input().strip())
  R = int(input().strip())

  G = [[] for _ in range(N)]
  for _ in range(R):
    u, v = map(int, input().strip().split())
    G[u].append((v, 1))
    G[v].append((u, 1))

  s, d = map(int, input().strip().split())

  path, cost = ga.floydWarshall(G)
  maxi = 0
  farthest = 0
  for i in range(N):
    if path[s][i] != -1 and path[s][i] != d:
      if cost[s][i] > maxi:
        maxi = cost[s][i]
        farthest = i
  for i in range(N):
    if path[d][i] != -1 and path[s][i] != s:
      if cost[d][i] > maxi:
        maxi = cost[d][i]
        farthest = i

  print(f"case {case + 1}: {cost[farthest][s] + cost[farthest][d]}")