import random

print("1. feladat")
rnd = random.choice(["F", "I"])
print("A pénzfeldobás eredménye: {}".format(rnd))

print("2. feladat")
tipp = input("Tippeljen! (F/I)= ")
dobas = random.choice(["F", "I"])
print("A tipp: {}, a dobás eredménye {} volt".format(tipp, dobas))
if tipp == dobas:
    print("Ön eltalálta")
else:
    print("Ön nem találta el")

dobasok = []
fajlBe = open("kiserlet.txt", "r")
while True:
    kiserlet = fajlBe.readline().strip()
    if not kiserlet:
        break
    dobasok.append(kiserlet)
fajlBe.close()

print("3. feladat")
print("A kísérlet {} dobásból állt.".format(len(dobasok)))

print("4. feladat")
fejekSzama = 0
gyakorisag = 0
for d in dobasok:
    if d == 'F':
        fejekSzama += 1
gyakorisag = round(fejekSzama / len(dobasok) * 100, 2)
print("A kísérlet során a fej relatív gyakorisága {}% volt.".format(gyakorisag))

print("5. feladat")
ossz = 0
egesz = ""
for d in dobasok:
    egesz += d
ossz = egesz.count("IFFI")

print("A kísérlet során {} alkalommal dobtak pontosan két fejet egymás után".format(ossz))

print("6. feladat")
fajlBe = open("kiserlet.txt", "r")
index = 0
maximum = 0
maxh = 0
while True:
    dob = fajlBe.readline().strip()
    if not dob:
        break
    index += 1
    if dob == "F":
        db = 1
        while fajlBe.readline().strip() == "F":
            db += 1
        if db > maximum:
            maximum = db
            maxh = index
        index = index + db
fajlBe.close()
print("A leghosszabb tisztafej sorozat {} tagból állt, kezdete a(z) {} dobás.". format(maximum, maxh))

print("7. feladat")
#nem foglalkozunk vele



