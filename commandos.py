import graph_algorithms as ga

T = int(input().strip())

for caseNum in range(1, T+1):
    N = int(input().strip())
    G = [[] for _ in range(N)]
    R = int(input().strip())
    for _ in range(R):
        u, v = map(int, input().strip().split())
        G[u].append((v, 1))
        G[v].append((u, 1))

    s, d = map(int, input().strip().split())

    _, cost = ga.floydWarshall(G)

    maxi = 0
    farthest = 0
    for i in range(N):
      if cost[s][i] != float('inf') and i != d:
        if cost[s][i] > maxi:
          maxi = cost[s][i]
          farthest = i
    for i in range(N):
      if cost[d][i] != float('inf') and i != s:
        if cost[d][i] > maxi:
          maxi = cost[d][i]
          farthest = i

    print(f"Case {caseNum}: {cost[farthest][s] + cost[farthest][d]}")