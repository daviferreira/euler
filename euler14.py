def iterative_sequence(n):
  sequence = []

  while n > 1:
    sequence.append(n)
    if n % 2 == 0:
      n /= 2
    else:
      n = n * 3 + 1

  sequence.append(1)
  return sequence

longest_chain = 1
for x in range(1, 1000000):
  chain_size = len(iterative_sequence(x))
  if chain_size > longest_chain:
    longest_chain = chain_size 
    print x
