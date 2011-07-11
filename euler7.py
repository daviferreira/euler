import math

def is_prime_number(number):
  if number < 2:
    return False;
  elif number == 2:
    return True;
  else:
    for x in range(3, int(number ** 0.5)+1, 2):
      if number % x == 0:
        return False
    return True

number = 1 
count = 0

while count < 10001:
  number = number + 1
  if number == 2 or number % 2:
    if is_prime_number(number):
      count = count + 1

print number
