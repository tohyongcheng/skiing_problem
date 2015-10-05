def memoize(f):
    memo = {}
    def helper(x):
        if x not in memo:            
            memo[x] = f(x)
        return memo[x]
    return helper

def main():
  f = open('map.txt')
  out = f.readlines()

  size = out[0].strip().split(" ")
  n, m = map(lambda x: int(x), size)
  # print x,y

  grid = out[1:]
  for i in xrange(len(grid)):
    grid[i] = grid[i].strip().split(" ")
    grid[i] = map(lambda x: int(x), grid[i])

  def valid_neighbours(x, y):
    valid_neighbors = []
    if (x - 1) >= 0 and grid[x-1][y] < grid[x][y]:
      valid_neighbors.append([x-1,y])
    if (x + 1) < n and grid[x+1][y] < grid[x][y]:
      valid_neighbors.append([x+1,y])
    if (y - 1) >= 0 and grid[x][y-1] < grid[x][y]:
      valid_neighbors.append([x,y-1])
    if (y + 1) < m and grid[x][y+1] < grid[x][y]:
      valid_neighbors.append([x,y+1])
    return valid_neighbors

  neighbours = []
  for i in xrange(n):
    temp = []
    for j in xrange(m):
      temp.append(valid_neighbours(i,j))
    neighbours.append(temp)

  @memoize
  def get_longest_path(coords):
    i,j = coords
    if len(neighbours[i][j]) == 0:
      return [(i,j)]
    else:
      max_path = []
      for n in neighbours[i][j]:
        ni,nj = n
        temp_path = get_longest_path((ni,nj))
        if len(temp_path) > len(max_path):
          max_path = temp_path
        elif len(max_path) == len(temp_path) and compute_depth([(i,j)] + temp_path) > compute_depth([(i,j)] + max_path):
          max_path = temp_path
      return [(i,j)] + max_path

  def compute_depth(path):
    i,j = path[0]
    first = grid[i][j]
    i,j = path[-1]
    last = grid[i][j]
    return first - last

  max_path = []
  for i in xrange(n):
    for j in xrange(m):
      temp_path = get_longest_path((i,j))
      if len(temp_path) > len(max_path):
        max_path = temp_path
      elif len(max_path) == len(temp_path) and compute_depth([(i,j)] + temp_path) > compute_depth([(i,j)] + max_path):
        max_path = temp_path
  print "The answer is", str(len(max_path)) + str(compute_depth(max_path))


main()


