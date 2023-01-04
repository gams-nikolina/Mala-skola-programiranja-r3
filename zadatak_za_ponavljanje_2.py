#2. zadatak za ponavljanje: Napiši program koji unosi riječ i ispisuje koliko puta se u njoj javlja samoglasnik "a".
a = input('Upiši riječ:')
p = 0
for i in a:
 if i in 'aA':
  p += 1
print (p)