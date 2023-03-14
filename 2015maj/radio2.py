class Uzenet:
    nap = 0
    amator = 0
    szoveg = ""

    def __init__(self, nap, amator, szoveg):
        self.nap = nap
        self.amator = amator
        self.szoveg = szoveg

print("1. feladat")
uzenetek = []
fajlBe = open("veetel.txt", "r")

while True:
    elsoSor = fajlBe.readline().split()
    masodikSor = fajlBe.readline()
    if not elsoSor:
        break
    else:
        uzenetek.append(Uzenet(int(elsoSor[0]), int(elsoSor[1]), masodikSor))
fajlBe.close()

print("2. feladat")
print("Az első üzenet rögzítője: {}".format(uzenetek[0].amator))
print("Az utolsó üzenet rögzítője: {}".format(uzenetek[-1].amator))

print("3. feladat")
for u in uzenetek:
    if "farkas" in u.szoveg:
        print("{}. nap {}. rádióamatőr".format(u.nap, u.amator))

print("4. feladat")
for n in range(1, 12):
    amatorokSzama = 0
    for u in uzenetek:
        if n == u.nap:
            amatorokSzama += 1
    print("{}. nap: {} rádióamatőr".format(n, amatorokSzama))
print("5. feladat")
print("6. feladat")
def szame(szo):
    valasz = True
    for i in range(len(szo)):
        if szo[i] < '0' or szo[i] > '9':
            valasz = False
    return valasz

print("7. feladat")
napIn = int(input("Adja meg a nap sorszámát! "))
amatorIn = int(input("Adja meg a rádióamatőr sorszámát! "))
vanE = True
for u in uzenetek:
    if u.nap == napIn and u.amator == amatorIn:
        vanE = True
        szo = u.szoveg.split()[0]
        if "/" in szo:
            szamok = szo.split("/")
            if szame(szamok[0]) and szame(szamok[1]):
                print("A megfigyelt egyedek száma: {}".format(int(szamok[0])+int(szamok[1])))
            else:
                print("Nincs információ")
        elif "#" in szo:
            print("Nincs információ")
        break
    else:
        vanE = False
if not vanE:
    print("Nincs ilyen feljegyzés")