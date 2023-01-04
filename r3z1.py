#1. Napiši program koji će ti omogućiti pogađanje lozinke. Program omogućava da se može pogađati lozinka sve dok se ne pogodi, a kada se pogodi lozinka ispiše se: "Upisali ste točnu lozinku! :)". Svaki puta kada se unese kriva lozinka ispiše se poruka: "Unijeli ste netočnu lozinku! :(". Lozinka neka bude po vašem izboru!
lozinka = ""
while lozinka != "pas123":
    lozinka = input("Unesite lozinku: ")
    if lozinka == "pas123":
        print("Upisali ste točnu lozinku! :)")
    else:
        print("Upisali ste netočnu lozinku! :( ")