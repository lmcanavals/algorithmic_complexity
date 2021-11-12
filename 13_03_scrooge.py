import graph_algorithms as ga

C = int(input().strip())

for _ in range(C):
  P = int(input().strip())
  locations = input().strip().split("\t")
  locationsDict = {loc: i for i, loc in enumerate(locations)}

  G = [[] for _ in range(P)]
  for u in range(P):
    line = map(int, input().strip().split("\t"))
    for v, w in enumerate(line):
      if w != 0 and w != -1:
        G[u].append((v, w))

  path, cost = ga.floydWarshall(G)

  R = int(input().strip())
  for _ in range(R):
    employee, source, target = input().strip().split()
    u = locationsDict[source]
    v = locationsDict[target]
    if path[u][v] == -1:
      print(f"Sorry Mr {employee} you can not go from {source} to {target}")
    else:
      print(f"Mr {employee} to go from {source} to {target}, you will receive {cost[u][v]} euros")
      route = []
      while u != v:
        route.append(locations[v])
        v = path[u][v]
      route.append(locations[v])
      strRoute = " ".join(reversed(route))
      print(f"Path: {strRoute}")