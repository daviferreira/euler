from helpers import factorial

def calculate_routes(grid_size):
  result = (factorial(2*grid_size))/(factorial(grid_size)**2) 
  return result

print calculate_routes(20)
