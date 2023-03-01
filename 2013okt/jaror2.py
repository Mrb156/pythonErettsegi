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