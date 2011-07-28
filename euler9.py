def is_pythagorean_triplet(a, b, c):
  return (a*a + b*b) == c*c

for a in range(1, 500):
  for b in range(1, 500):
    for c in range(1, 500):
      if is_pythagorean_triplet(a, b, c):
        if a + b + c == 1000:
          print a * b * c 
