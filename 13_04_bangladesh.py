import graph_algorithms as ga

def dist(a, b):
  x1, y1 = a
  x2, y2 = b
  return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

while True:
  N, M = map(int, input().split())
  if N == 0 and M == 0: break

  graph = [[] for _ in range(N)]
  positions = []

  cont = N
  while cont > 0:
    line = list(map(int, input().split()))
    pairs = [(line[i], line[i+1]) for i in range(0, len(line), 2)]
    cont -= len(pairs)
    positions.extend(pairs)

  cont = M
  while cont > 0:
    line = list(map(int, input().split()))
    pairs = [(line[i], line[i+1]) for i in range(0, len(line), 2)]
    cont -= len(pairs)
    for u, v in pairs:
      w = dist(positions[u-1], positions[v-1])
      graph[u-1].append((v-1, w))
      graph[v-1].append((u-1, w))
      
  _, preCost = ga.floydWarshall(graph)

  largest = 0
  chosenU = 0
  chosenV = 0
  for u in range(N):
    for v in range(N):
      if v not in graph[u]:
        w = dist(positions[u], positions[v])
        graph[u].append((v, w))
        graph[v].append((u, w))
        _, curCost = ga.floydWarshall(graph)
        C = 0
        for i in range(N):
          for j in range(N):
            C += preCost[i][j] - curCost[i][j]
        if C > largest:
          largest = C
          chosenU = u
          chosenV = v
        graph[u].pop()
        graph[v].pop()
        
  if largest == 0:
    print("No road required")
  else:
    print(chosenU+1, chosenV+1)
