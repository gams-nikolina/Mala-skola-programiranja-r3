#1. Zadatak za ponavljanje: Napiši program koji unosi osobno ime te ispisuje poruku je li učitano ime muško
#ili žensko. Ako ime zavrsava slovom ’a’ ispisat će se poruka "Žensko ime", a u svim ostalim
#slučajevima "Muško ime". Iznimke ćemo zanemariti.

ime=input('Upiši ime:  ')
if ime[-1]=='a':
    print('Žensko ime')
else:
    print('Muško ime')
