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











