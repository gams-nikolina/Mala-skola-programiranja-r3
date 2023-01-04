#2. Napravi igru koja ti omogućava pogađanje brojeva. Ukoliko upišeš broj 0 neka se dogodi prekid programa. Za prekid programa koristi naredbu break. Ukoliko korisnik upiše broj koji je veći ili manji od traženog broja neka mu izbaci prikladna poruka. Ukoliko pogodi točan broj neka mu se ispiše poruka: "Bravo! Pogodio/la si traženi broj!"
print ("Igra pogađanja brojeva!")
print ("Ukoliko želiš prekinuti igru pritisni 0")
tocanBroj=24

while 1:
    broj=int(input("Unesi broj: "))
    if broj==tocanBroj:
        print ("Bravo! Pogodio/la si traženi broj!")
        broj=0
        break
    elif broj==0:
        break
    elif broj > tocanBroj :
        print ("Traženi broj je manji od upisanog, pokušaj opet! ")
    elif broj < tocanBroj :
        print ("Traženi broj je veći od upisanog, pokušaj opet!")