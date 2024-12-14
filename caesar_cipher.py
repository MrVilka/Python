n = input(': ')
al = 'abcdefghijklmnopqrstuvwxyz'
alpha = []
for a in al:
  alpha += a
lenn = len(alpha)
print('Размер алфавита: ', lenn)
itog = ''
for i in n:
  for j in range(lenn):
    if i == alpha[j]:
      if(j + 4 <= lenn):
        a = alpha[j + 3]
        # print(j + 3)
        itog += a
      elif j + 4 > lenn:
        k = j + 3 - lenn
        itog += alpha[k]
        # print('Закинул', alpha[k],'-', k)
print(n,'  ->  ',itog)
