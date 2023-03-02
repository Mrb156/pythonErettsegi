class Cim:
    cim = ""
    tipus = ""
    def __init__(self, cim, tipus):
        self.cim = cim
        self.tipus = tipus

print("1. feladat")
fajlBe = open("ip.txt", "r")
cimek = []
tipusok = ["2001:0db8", "2001:0e", "fc", "fd"]

for i in range(500):
    sor = fajlBe.readline().strip()
    if not sor:
        break
    if sor.split(':')[0] == "2001" and sor.split(':')[1] == "0db8":
        curCim = Cim(sor, "dokumentációs cím")
        cimek.append(curCim)
    elif sor.split(':')[0] == "2001" and sor.split(':')[1] == "0e":
        curCim = Cim(sor, "globális egyedi cím")
        cimek.append(curCim)
    elif (sor.split(':')[0][0] == "f" and sor.split(':')[0][1] == "c") or (sor.split(':')[0][0] == "f" and sor.split(':')[0][1] == "d"):
        curCim = Cim(sor, "helyi egyedi cím")
        cimek.append(curCim)

print(cimek[3].tipus)

print("2. feladat")
print(len(cimek))

print("3. feladat")
minimum = cimek[0].cim

for c in cimek:
    ossz = 0
    for k in c.cim:
        if k != ':':
            ossz = ossz + int(ord(k))
    print(ossz)

print(minimum)
