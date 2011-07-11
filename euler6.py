n1 = 0
n2 = 0

for x in xrange(1, 101):
	n1 += x*x
	n2 += x

print n2 * n2 - n1
