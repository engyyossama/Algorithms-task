def prim(G, s):
      cost_value = [float("inf")] * len(G) 
      cost_value[s] = 0
      itr = [False] * len(G)
      c = 0
      while True: 
            mw = float("inf")
            m_idx = -1
            for i in range(len(G)): 
                  if itr[i] == False:
                        if cost_value[i] < mw: 
                              mw = cost_value[i] 
                              m_idx = i
            if m_idx == -1: 
                  break
            c += mw 
            itr[m_idx] = True
            for i, j in G[m_idx].items():
                  cost_value[i] = min(cost_value[i], j)
      return c


def call(n, e, s):
      G = {i: {} for i in range(n)}
      for item in e:
            x = item[0]
            z = item[1]
            weight = item[2]
            x -= 1
            z -= 1
            try: 
                  mw = min(G[x][z], weight)
                  G[x][z] = mw
                  G[z][x] = mw
            except KeyError:
                  G[x][z] = weight
                  G[z][x] = weight
      return prim(G, s)
