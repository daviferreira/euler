import math

def is_evenly_divisible(num):
	evenly_divisible = True
	for x in xrange(20, 10, -1):
		if num % x:
			evenly_divisible = False
			break
	return evenly_divisible

num = 5040 
evenly_divisible = False
while not evenly_divisible:
	evenly_divisible = is_evenly_divisible(num)
	if not evenly_divisible:
		num = num + 2520

print num