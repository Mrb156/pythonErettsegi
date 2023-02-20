class Data:
    sorszam = 0
    szavazat = 0
    vezetekN = ""
    utoN = ""
    part = ""

    def __init__(self, sorszam, szavazat, vezetekn, uton, part):
        self.sorszam = sorszam
        self.szavazat = szavazat
        self.vezetekN = vezetekn
        self.utoN = uton
        self.part = part


print("1. feladat")
file = open("szavazatok.txt", "r")
valaszt = []

for i in range(100):
    adatsor = file.readline().strip().split()
    if not adatsor:
        break
    adat = Data(int(adatsor[0]), int(adatsor[1]), adatsor[2], adatsor[3], adatsor[4])
    valaszt.append(adat)

print("Kesz")
print("2. feladat")
print("A képviselőválasztásokon {} képviselő indult.".format(len(valaszt)))

print("3. feladat")
veztekInput = input("Kérem a vezetéknevet\n")
utoInput = input("Kérem az utónevet\n")
vanE = False
szavDb = 0

for szav in valaszt:
    if szav.vezetekN == veztekInput and szav.utoN == utoInput:
        vanE = True
        szavdb = szav.szavazat
        break
if vanE:
    print("Az illető {} szavazatot kapott.".format(szavDb))
else:
    print("Ilyen képviselő nincs")

print("4. feladat")
polgarok = 12345
szavazatokDB = 0
for szav in valaszt:
    szavazatokDB = szavazatokDB+szav.szavazat

arany = round(szavazatokDB/polgarok*100, 2)
print("A választáson {} állampolgár, a jogosultak {}%-a vett részt.".format(polgarok, arany))

print("5. feladat")
partok = ["GYEP", "HEP", "TISZ", "ZEP", "-"]
for p in partok:
    partSzav = 0
    for v in valaszt:
        if v.part == p:
            partSzav = partSzav+v.szavazat
    partArany = round(partSzav/szavazatokDB*100, 2)
    if p == "-":
        print("Független jelöltek = {}%".format(partArany))
    else:
        print("{} = {}%".format(p, partArany))

print("6. feladat")
maxx = 0
for v in valaszt:
    if v.szavazat > maxx:
        maxx = v.szavazat
for v in valaszt:
    if v.szavazat == maxx and v.part != "-":
        print("{} {} {}".format(v.vezetekN, v.utoN, v.part))
    elif v.szavazat == maxx:
        print("{} {} Független".format(v.vezetekN, v.utoN))

print("7.feladat")
fajl = open("kepviselok2.txt", "w")

for i in range(1, 9):
    maxx = 0
    for v in valaszt:
        if v.sorszam == i and v.szavazat > maxx:
            maxx = v.szavazat
    for v in valaszt:
        if v.sorszam == i and v.szavazat == maxx and v.part != "-":
            fajl.write("{} {} {} {}\n".format(i, v.vezetekN, v.utoN, v.part))
        elif v.sorszam == i and v.szavazat == maxx:
            fajl.write("{} {} {} független\n".format(i, v.vezetekN, v.utoN))
print("kesz")
