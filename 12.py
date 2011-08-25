from helpers import *

i = 1 
divisors = 0
while divisors <= 500:
  n = triangle_number(i) 
  print n
  divisors = divisors_count(n)
  i += 1
