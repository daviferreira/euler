def triangle_number(n):
  return (n * (n + 1)) / 2

def divisors_count(n):
  count = 1
  factors = prime_factorization(n)
  for x in factors:
    count *= factors[x] + 1
  return count 

def is_prime_number(n):
  if n < 2:
    return False
  elif n == 2:
    return True
  else:
    for x in range(3, int(n ** 0.5)+1, 2):
      if n % x == 0:
        return False
    return True

def factors(n):
  factors = [] 
  for x in range(n, 0, -1):
    factors.append(x)
  return factors

def factorial(n):
  factors_list = factors(n)
  factorial = 1
  for x in factors_list:
    factorial *= x
  return factorial 

def prime_factorization(n):
  prime_factors = {} 
  x = 2 
  while n > 1:
    if is_prime_number(x) and n % x == 0:
      if x in prime_factors:
        prime_factors[x] += 1
      else:
        prime_factors[x] = 1
      n /= x
      x = 2 
    else:
      x += 1
  return prime_factors
