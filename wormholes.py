import graph_algorithms as ga

c = int(input().strip())
while c > 0:
  c -= 1
  n, m = map(int, input().strip().split())
  g = ga.Digraph(n)
  while m > 0:
    m -= 1
    x, y, t = map(int, input().strip().split())
    ga.addDiEdge(g, x, y, t)

  p, d = ga.bellmanFord(g, 0)
  print("possible" if p is None else "not possible")