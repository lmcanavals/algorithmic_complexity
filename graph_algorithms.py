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
  dist = [float('inf')]*n
  dist[s] = 0
  path = [-1]*n

  # relax edges
  for _ in range(n-1):
    for u in range(n):
      for v, w in G[u]:
        # relax edge (u, v)
        f = dist[u] + w
        if f < dist[v]:
          dist[v] = f
          path[v] = u

  # check for negative-weight cycles
  for u in range(n):
    for v, w in G[u]:
      if dist[u] + w < dist[v]:
        return None, None

  return path, dist

def Digraph(n):
  G = [[] for _ in range(n)]
  return G

def addDiEdge(G, u, v, w):
  G[u].append((v, w))

