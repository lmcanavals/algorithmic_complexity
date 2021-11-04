import graph_algorithms as ga

c = int(input().strip())

while c > 0:
  c -= 1

  n, m = map(int, input().strip().split())
  G = [[] for _ in range(n)]
  for _ in range(m):
    x, y, t = map(int, input().strip().split())
    G[x].append((y, t))

  ok, _ = ga.bellmanFord(G, 0)
  print("possible" if not ok else "not possible")