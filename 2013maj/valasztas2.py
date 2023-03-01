class Kepviselo:
    kerulet = 0
    szavazatok = 0
    vezetekN = ""
    utoN = ""
    part = ""

    def __init__(self, kerulet, szavazatok, vezetekN, utoN, part):
        self.kerulet = kerulet
        self.szavazatok = szavazatok
        self.vezetekN = vezetekN
        self.utoN = utoN
        self.part = part

print("1. feladat")
file = open("szavazatok.txt", "r")
kepviselok = []

for i in range(100):
    adatsor = file.readline().strip().split()
    if not adatsor:
        break
    kepviselo = Kepviselo(int(adatsor[0]), int(adatsor[1]), adatsor[2], adatsor[3], adatsor[4])
    kepviselok.append(kepviselo)
file.close()
print("Kész a beolvasás")

print("2. feladat")
print("A helyhatósági választáson {} képviselőjelölt {}.".format(len(kepviselok), "indult"))

print("3. feladat")
bekerVezetekN = input("Adjon meg egy vezetéknevet: ")
bekerUtoN = input("Adjon meg egy utónevet: ")
szavazatDB = 0
vanE = False

for k in kepviselok:
    if k.vezetekN == bekerVezetekN and k.utoN == bekerUtoN:
        vanE = True
        szavazatDB = k.szavazatok
        break
if vanE:
    print("Az illető {} szavazatot kapott".format(szavazatDB))
else:
    print("Ilyen nevű képviselőjelölt nem szerepel a nyilvántartásban!")

print("4. feladat")
polgarokSzama = 12345
szavatokSzama = 0

for k in kepviselok:
    szavatokSzama = szavatokSzama+k.szavazatok
arany = round(szavatokSzama/polgarokSzama*100, 2)

print("A választáson {} állampolgár, a jogosultak {}%-a vett részt.".format(szavatokSzama, arany))

print("5. feladat")
partok = ["GYEP", "HEP", "TISZ", "ZEP", "-"]

for p in partok:
    partSzavazatokSzama = 0
    for k in kepviselok:
        if k.part == p:
            partSzavazatokSzama = partSzavazatokSzama+k.szavazatok
    partArany = round(partSzavazatokSzama/szavatokSzama*100, 2)
    if p == "GYEP":
        print("Gyümölcsevők Pártja = {}%".format(partArany))
    elif p == "HEP":
        print("Húsevők Pártja = {}%".format(partArany))
    elif p == "TISZ":
        print("Tejivók Szövetsége = {}%".format(partArany))
    elif p == "ZEP":
        print("Zöldségevők Pártja = {}%".format(partArany))
    else:
        print("Független jelöltek = {}%".format(partArany))

print("6. feladat")
maximum = 0
for k in kepviselok:
    if k.szavazatok > maximum:
        maximum = k.szavazatok
for k in kepviselok:
    if k.szavazatok == maximum and k.part != "-":
        print("{} {} {}".format(k.vezetekN, k.utoN, k.part))
    elif k.szavazatok == maximum and k.part == "-":
        print("{} {} független".format(k.vezetekN, k.utoN))

print("7. feladat")
fileWrite = open("kepviselok.txt", "w")

for i in range(1, 9):
    maximum = 0
    for k in kepviselok:
        if k.kerulet == i and k.szavazatok > maximum:
            maximum = k.szavazatok
    for k in kepviselok:
        if k.kerulet == i and k.szavazatok == maximum and k.part != "-":
            fileWrite.write("{} {} {} {}\n".format(i, k.vezetekN, k.utoN, k.part))
        elif k.kerulet == i and k.szavazatok == maximum and k.part == "-":
            fileWrite.write("{} {} {} független\n".format(i, k.vezetekN, k.utoN))
print("kész")