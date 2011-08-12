import math
from helpers import *

sum_primes_below_two_million = 0

for x in xrange(2000000):
  if x == 2 or x % 2:
    if is_prime_number(x):
      sum_primes_below_two_million += x

print sum_primes_below_two_million
