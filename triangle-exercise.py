with open('./triangle.txt') as f:
    content = f.readlines()
triangle = [x.strip().split() for x in content]

def maximumSum(triangle):
  for i in range(1, len(triangle)):
    for j in range(0, len(triangle[i])):
      if j == 0:
        triangle[i][j] += triangle[i-1][j]
      elif j == len(triangle[i]) - 1:
        triangle[i][j] += triangle[i-1][j-1]
      else:
        triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])
  print(max(triangle[-1]))
  return

maximumSum(triangle)