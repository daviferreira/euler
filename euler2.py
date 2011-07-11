import math

def sequencia_fibonacci():
  x, y = 0, 1
  while True:
    yield x
    x, y = y, x+y

def numero_par(sequencia):
  for numero in sequencia:
    if not numero % 2:
      yield numero

def abaixo_de_quatro_milhoes(sequencia):      
  for numero in sequencia:
    if numero > 4000000:
      break
    yield numero

print sum(numero_par(abaixo_de_quatro_milhoes(sequencia_fibonacci())))
