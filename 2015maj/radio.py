class Uzenet:
    nap = 0
    amator = 0
    szoveg = ""

    def __init__(self, _nap, _amator, _szoveg):
        self.nap = _nap
        self.amator = _amator
        self.szoveg = _szoveg


print("1. feladat")
uzenetek = []
fajlBe = open("veetel.txt", "r")

while True:
    elsoSor = fajlBe.readline().strip().split()
    masodikSor = fajlBe.readline()
    if not elsoSor:
        break
    else:
        uzenetek.append(Uzenet(int(elsoSor[0]), int(elsoSor[1]), masodikSor))
fajlBe.close()

print("2. feladat")
print("{} számú rádióamatőr rögzítette az első üzenetet".format(uzenetek[0].amator))
print("{} számú rádióamatőr rögzítette az utolsó üzenetet".format(uzenetek[-1].amator))

print("3. feladat")
for u in uzenetek:
    if "farkas" in u.szoveg:
        print("{}. nap {}. rádióamatőr".format(u.nap, u.amator))

print("4. feladat")
for i in range(1, 12):
    fejlegyzesekSZama = 0
    for u in uzenetek:
        if u.nap == i:
            fejlegyzesekSZama += 1
    print("{}. nap: {} rádióamatőr".format(i, fejlegyzesekSZama))

print("5. feladat")
# kimarad

print("6. feladat")
def szame(szo):
    valasz = True
    for i in range(len(szo)):
        if szo[i] < '0' or szo[i] > '9':
            valasz = False
    return valasz

print("7. feladat")
napIn = int(input("Adja meg a nap sorszámát!"))
amatorIn = int(input("Adja meg a rádióamatőr sorszámát!"))
vanE = True
for u in uzenetek:
    if u.nap == napIn and u.amator == amatorIn:
        vanE = True
        szo = u.szoveg.split(" ")[0]
        if "/" in szo:
            szoEll = szo.split('/')
            if szame(szoEll[0]) and szame(szoEll[1]):
                print("A megfigyelt egyedek száma: {}".format(int(szoEll[0]) + int(szoEll[1])))
            else:
                print("Nincs információ")
        elif "#" in szo:
            print("Nincs információ")
        break
    else:
        vanE = False
if not vanE:
    print("Nincs ilyen feljegyzés")

