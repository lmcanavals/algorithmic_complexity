def Digraph(n):
  G = [[] for _ in range(n)]
  return G

def addDiEdge(G, u, v, w):
  G[u].append((v, w))

def bfs(G, s):
  n = len(G)
  visited = [False]*n
  parent = [None]*n
  queue = [s]
  visited[s] = True

  while queue:
    u = queue.pop(0)
    for v in G[u]:
      if not visited[v]:
        visited[v] = True
        parent[v] = u
        queue.append(v)

  return parent


def dfs(G, s):
  n = len(G)
  visited = [False]*n
  parent = [None]*n

  def _dfs(u):
    visited[u] = True
    for v in G[u]:
      if not visited[v]:
        parent[v] = u
        _dfs(v)

  _dfs(s)

  return parent

import heapq as hq

def dijkstra(G, s):
  n = len(G)
  cost = [float('inf')]*n
  cost[s] = 0
  path = [-1]*n
  visited = [False]*n

  queue = [(0, s)]

  while queue:
    c, u = hq.heappop(queue)
    if visited[u]: continue
    visited[u] = True
    for v, w in G[u]:
      if not visited[v] and c + w < cost[v]:
        cost[v] = c + w
        path[v] = u
        hq.heappush(queue, (cost[v], v))

  return path, cost

def bellmanFord(G, s):
  n = len(G)

  # initialize
  cost = [float('inf')]*n
  cost[s] = 0
  path = [-1]*n

  # relax
  for _ in range(n-1):
    for u in range(n):
      for v, w in G[u]:
        if cost[u] + w < cost[v]:
          cost[v] = cost[u] + w
          path[v] = u

  # check negative cycle
  for u in range(n):
    for v, w in G[u]:
      if cost[u] + w < cost[v]:
        return None, None # negative cycle exists

  return path, cost

def floydWarshall(G):
  n = len(G)

  # initialize
  cost = [[float('inf')]*n for _ in range(n)]
  path = [[-1]*n for _ in range(n)]


  for u in range(n):
    cost[u][u] = 0
    for v, w in G[u]:
      cost[u][v] = w
      path[u][v] = u

  # relax
  for k in range(n):
    for i in range(n):
      if i == k: continue
      for j in range(n):
        if j == k or j == i: continue
        f = cost[i][k] + cost[k][j]
        if f < cost[i][j]:
          cost[i][j] = f
          path[i][j] = path[k][j]

  return path, cost

def johnson(G):
  n = len(G)

  # initialize
  G.append([(n-1, 0)])

  # aplicar bellman ford
  _, g = bellmanFord(G, n)
  
  if not g: return None

  # initialize

  # create G'
  Gprime = [[] for _ in range(n)]
  for u in range(n):
    for v, w in G[u]:
      Gprime[u].append((v, w + g[u] - g[v])) # :O

  # dijkstra empezando en cada vertice
  path = []
  for u in range(n):
    p, _ = dijkstra(Gprime, u)
    path.append(p)


  # eliminar ultimo vertice
  G.pop()

  return path