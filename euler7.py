import math
from helpers import *

number = 1 
count = 0

while count < 10001:
  number = number + 1
  if number == 2 or number % 2:
    if is_prime_number(number):
      count = count + 1

print number
