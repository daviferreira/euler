import math

def multiples_of_3_or_5():
  for n in xrange(1000):
    if not n % 3  or not n % 5: 
      yield n

print sum(multiples_of_3_or_5())
