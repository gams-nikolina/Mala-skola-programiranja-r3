#3. Napravi kalkulator koji će ti omogućiti izabiranje jedne od četiri računske operacije (zbrajanje, oduzimanje, množenje i dijeljenje). Nakon odabira  računske operacije kalkulator ti nudi opciju unosa 2 broja te izbacuje rješenje. (Hint: svakoj računskoj operaciji dodaj jedan broj - npr. 1.Zbrajanje)
izbor = 0
while 1:
    print ("Python kalkulator")
    print ("Izaberi računsku operaciju: ")
    print (" ")
    print (" 1. Zbrajanje")
    print (" 2. Oduzimanje")
    print (" 3. Množenje")
    print (" 4. Dijeljenje")
    print(" 5. Izađi iz kalkulatora")

    izbor = int(input("Unesi broj ispred željene računske operacije: "))

    if izbor == 1:
        zbrajanje1 = int(input("Zbroji ovaj broj: "))
        zbrajanje2 = int(input("s ovim brojem: "))
        print (zbrajanje1, "+", zbrajanje2, "=", zbrajanje1+zbrajanje2)
    elif izbor == 2:
        oduzimanje1 = int(input("Oduzmi od ovog broja: "))
        oduzimanje2 = int(input("ovaj broj: "))
        print(oduzimanje1, "-", oduzimanje2, "=", oduzimanje1-oduzimanje2)
    elif izbor == 3:
        mnozenje1 = int(input("Pomnoži ovaj broj: "))
        mnozenje2 = int(input("s ovim brojem: "))
        print(mnozenje1, "*", mnozenje2, "=", mnozenje1 * mnozenje2)
    elif izbor == 4:
        dijeljenje1 = int(input("Podijeli ovaj broj: "))
        dijeljenje2 = int(input("s ovim brojem: "))
        print(dijeljenje1, "/", dijeljenje2, "=", dijeljenje1 / dijeljenje2)
    elif izbor == 5:
        break
        print("Hvala što koristiš Python kalkulator! :) ")