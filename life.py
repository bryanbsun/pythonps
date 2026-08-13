def glider():
  grid = []
  grid.append([0,1,0,0,0,0,0,0,0,0])
  grid.append([0,0,1,0,0,0,0,0,0,0])
  grid.append([1,1,1,0,0,0,0,0,0,0])
  grid.append([0,0,0,0,0,0,0,0,0,0])
  grid.append([0,0,0,0,0,0,0,0,0,0])
  grid.append([0,0,0,0,0,0,0,0,0,0])
  grid.append([0,0,0,0,0,0,0,0,0,0])
  grid.append([0,0,0,0,0,0,0,0,0,0])
  grid.append([0,0,0,0,0,0,0,0,0,0])
  grid.append([0,0,0,0,0,0,0,0,0,0])
  return grid

g1 = glider()
print(len(g1))
for g in g1:
    print(g)
