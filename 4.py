largest_palindromic = 0

for a in xrange(999, 100, -1):
  for b in xrange(a, 100, -1):
    x = a * b
    if x > largest_palindromic:
      x = str(x)
      if x == x[::-1]:
        largest_palindromic = a * b

print largest_palindromic