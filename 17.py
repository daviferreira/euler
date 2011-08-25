import re

numbers = (
  ('', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen'),
  ('', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety')
)

def number_to_words(n):
  if n < 20:
    return numbers[0][n]
  if n == 1000:
    return "one thousand" 
  elif n % 100 == 0:
    return numbers[0][int(str(n)[0:1])] + " hundred"
  elif n < 100:
    if n % 10 == 0: 
      return numbers[1][int(str(n)[0:1])]
    else:
      n = str(n)
    n1 = numbers[1][int(n[0:1])]
    n2 = numbers[0][int(n[1:2])]
    n = n1 + "-" + n2
    return n
  else:
    n = str(n)
    n1 = numbers[0][int(n[0:1])]
    verifier = int(n[1:3])
    if verifier >= 20:
      n2 = numbers[1][int(n[1:2])]
      n3 = numbers[0][int(n[2:3])]
      n = n1 + " hundred and " + n2
      if n3 != "":
        n += "-" + n3
    else:
      n = n1 + " hundred and " + numbers[0][verifier]
    return n
      
total = 0
for x in range(1, 1001):
  total += len(re.sub('[^a-z]', '', number_to_words(x)))

print total
