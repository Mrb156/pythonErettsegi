class Jarmu:
    ora = 0
    perc = 0
    masodperc = 0
    rendsz = ""

    def __init__(self, _ora, _perc, _masodperc, _rendsz):
        self.ora = _ora
        self.perc = _perc
        self.masodperc = _masodperc
        self.rendsz = _rendsz


print("1. feladat")

file = open("jarmu.txt", "r")
meresek = []
while True:
    sor = file.readline().strip().split()
    if not sor:
        break
    jarmu = Jarmu(int(sor[0]), int(sor[1]), int(sor[2]), sor[3])
    meresek.append(jarmu)
print("kesz")

print("2. feladat")
munkaIdo = meresek[-1].ora - meresek[0].ora
print("A munkaidő legalább {} óra volt.".format(munkaIdo))

print("3. feladat")
ora = meresek[0].ora - 1
for m in meresek:
    if ora < m.ora:
        print("{} óra: {}".format(m.ora, m.rendsz))
        ora += 1

print("4. feladat")
B = 0
K = 0
M = 0
for m in meresek:
    if m.rendsz[0] == "B":
        B += 1
    elif m.rendsz[0] == "K":
        K += 1
    elif m.rendsz[0] == "M":
        M += 1
print("Autóbusz: {}\nKamion: {}\nMotor: {}".format(B, K, M))

print("5. feladat")
maximum = 0
ido1 = []
ido2 = []
for i in range(len(meresek) - 1):
    curTime = ((meresek[i + 1].ora - meresek[i].ora) * 60) \
              + (meresek[i + 1].perc - meresek[i].perc) \
              + ((meresek[i + 1].masodperc -meresek[i].masodperc) / 60)
    if curTime > maximum:
        maximum = curTime
        ido1 = [meresek[i].ora, meresek[i].perc, meresek[i].masodperc]
        ido2 = [meresek[i + 1].ora, meresek[i + 1].perc, meresek[i + 1].masodperc]
print(maximum)
print("{}:{}:{} - {}:{}:{}".format(ido1[0], ido1[1], ido1[2], ido2[0], ido2[1], ido2[2]))

print("6.feladat")
beker = input("Adjon meg egy rendszámot: ")
for m in meresek:
    talalat = True
    for i in range(len(beker)):
        talalat = talalat and (beker[i] == m.rendsz[i] or beker[i] == '*')
    if talalat:
        print(m.rendsz)

print("7. feladat")

fileOutput = open("vizsgalt.txt", "w")
vizsgkezd = -300

for m in meresek:
    if vizsgkezd+300<=((m.ora*60+m.perc)*60+m.masodperc):
        fileOutput.write("{} {} {} {}\n".format(m.ora, m.perc, m.masodperc, m.rendsz))
        vizsgkezd = ((m.ora*60+m.perc)*60+m.masodperc)


