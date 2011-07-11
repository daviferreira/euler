import math

def multiplos_de_3_ou_5():
  for n in xrange(1000):
    if not n % 3  or not n % 5: 
      yield n

print sum(multiplos_de_3_ou_5())
