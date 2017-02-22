def approx(f, a, b): # to approximate area of func f from a --> b by Simpson
  ar = ((b - a) / 6) * (f(a) + 4 * f((a - b) / 2) + f(b))
  return ar

def simpson_sum(f, a, b, n): # sums up approximations on interval a to b of function f
  
  s, diff = 0, (b - a)/n
  
  i = a
  while((i <= b and b > a) or (a > b and i <= a)):
    s += approx(f, i, i + diff)
    i += diff
  
  return s
