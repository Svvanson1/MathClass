def print_mat(mat):
  s = ""
  for i in range(len(mat)):
    s += "[ "
    for k in range(len(mat[0])):
      if(k == len(mat[0]) - 1):
        s+= "| "
      s += str(mat[i][k]) + " "
    s += "]\n"
  print(s)

def triangular_form(matrix, n, m):  # puts matrix into triangular form
  for i in range(m - 1):  # to loop through the equations apart from the last column
    for j in range(i+1, m):
      mult = matrix[j][i]/matrix[i][i]
      for k in range(n+1):
        matrix[j][k] = matrix[j][k] - mult*matrix[i][k]
  return True

def solve_eq(mat, n, m):
  for i in range(m - 1, -1, -1):
    for j in range(i, n - 1):
      mat[i][n] -= mat[i][j+1] * mat[j+1][n]
      mat[i][j+1] = 0.0
    mat[i][n] = mat[i][n]/mat[i][i]
    mat[i][i] = 1
  return True

def solve_linear_system(mat):
  m = len(mat)  # equations
  n = len(mat[0]) - 1  # unknowns 
  
  if(n > m):
    return False
  triangular_form(mat, n, m)
  solve_eq(mat, n, m)
  
  return True
''' testing purposes 
def main():
  matrix = [[1.0, -3.0, 5.0, -9.0], [2.0, -1.0, -3.0, 19.0], [3.0, 1.0, 4.0, -13.0]]
  solve_linear_system(matrix)
  print_mat(matrix)
main()'''
