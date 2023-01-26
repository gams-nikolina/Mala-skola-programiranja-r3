#2. Napravi igru koja ti omogućava pogađanje brojeva.Ukoliko korisnik upiše broj koji je veći ili manji od traženog broja neka mu izbaci prikladna poruka. Ukoliko pogodi točan broj neka mu se ispiše poruka: "Bravo! Pogodio/la si traženi broj!"
print ("Igra pogađanja brojeva!")
tocanBroj=24
while 1:
    broj=int(input("Unesi broj: "))
    if broj==tocanBroj:
        print ("Bravo! Pogodio/la si traženi broj!")
      
    elif broj > tocanBroj :
        print ("Traženi broj je manji od upisanog, pokušaj opet! ")
    elif broj < tocanBroj :
        print ("Traženi broj je veći od upisanog, pokušaj opet!")
