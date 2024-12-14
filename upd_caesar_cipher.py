n = input(': ')
al = 'abcdefghijklmnopqrstuvwxyz'
alpha = []
itog = ''
d = ''
up = []

for a in al:
  alpha += a
lena = len(alpha)

words = n.split(' ')

n2 = n.lower()

words2 = n2.split()
lenn = len(words2)

up = [1 if word.istitle() else 0 for word in words]
print(up)

for a in range(lenn):
  for b in words2[a]:
    for c in range(lena):
      if b == alpha[c]:
          if c + 4 <= lena:
            itog += alpha[c + 3]
          elif c + 4 > lena:
            k = c + 3 - lena
            itog += alpha[k]
  itog += ' '
print(itog)
