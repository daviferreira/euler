import math

def fibonacci_sequence():
  x, y = 0, 1
  while True:
    yield x
    x, y = y, x+y

def even_number(sequence):
  for numero in sequence:
    if not numero % 2:
      yield numero

def under_four_million(sequence):      
  for numero in sequence:
    if numero > 4000000:
      break
    yield numero

print sum(even_number(under_four_million(fibonacci_sequence())))
