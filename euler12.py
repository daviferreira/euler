from helpers import *

i = 1 

while True:
  n = triangle_number(i) 
  print n
  if divisors_count(n) > 500:
    print n
    break
  i += 1
