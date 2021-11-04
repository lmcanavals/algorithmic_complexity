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
        return None, None

  return path, cost

def floydWarshall(G):
  n = len(G)
  cost = [[float('inf')]*n for _ in range(n)]
  path = [[-1]*n for _ in range(n)]

  for u in range(n):
    for v, w in G[u]:
      cost[u][v] = w
      path[u][v] = u

  for k in range(n):
    for i in range(n):
      for j in range(n):
        if i != j and j != k and i != k:
          f = cost[i][k] + cost[k][j]
          if f < cost[i][j]:
            cost[i][j] = f
            path[i][j] = path[k][j]

  return path, cost