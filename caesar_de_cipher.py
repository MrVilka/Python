print('Программа - ДЕШИФРАТОР Цезаря \n')
n = input(': ')
al = 'abcdefghijklmnopqrstuvwxyz'
alpha = []
for a in al:
  alpha += a
lenn = len(alpha)
itog = ''
print('Размер алфавита: ', lenn)

for a in n:
  for b in range(lenn):
    if a == alpha[b]:
      itog += alpha[b - 3]
print(itog)
