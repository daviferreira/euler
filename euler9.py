import sys

def is_pythagorean_triplet(a, b, c):
  return (a*a + b*b) == c*c

for a in range(1, 1000):
  for b in range(1, 1000):
    c = 1000 - a - b
    if c > 0 and is_pythagorean_triplet(a, b, c):
      if a + b + c == 1000:
        print a * b * c 
        sys.exit()
