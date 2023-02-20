szam = 5
szoveg = "ez egy szöveg"
karakter = 'h'
tizedes = 20.45
logikaiIgaz = True
logikaiHamis = False

valtozo = ""
int = 2
string = "sdf"
float_double = 20.4
bool = True

tombSzam = [2,3,4,5]
tombSzoveg = ["sdf2","sfds3","4sf"]
ures = []
# print(tombSzoveg[1] + tombSzam[0])
# print("ez egy szöveg {}, ez pedig egy szám {}".format(tombSzoveg[1], tombSzam[0]))
a = input("Kérem adjon meg egy számot:")
b = input("Kérem adjon meg egy számot:")

class Kepviselo:
    kerulet = 0
    szavazatDb = 0
    vezetekN = ""
    keresztN = ""
    part = ""

    def __init__(self, kerulet, szavazatDb, vezetekN, keresztN, part):
        self.kerulet = kerulet
        self.szavazatDb = szavazatDb
        self.vezetekN = vezetekN
        self.keresztN = keresztN
        self.part = part



kepviselo1 = Kepviselo(5, 19, "Ablak", "Antal", "-")
print("vezeteknév: {} | keresztnév: {}".format(kepviselo1.vezetekN,kepviselo1.keresztN))

tombSzam = [2,3,4,5,6]

# for i in range(len(tombSzam)):
#     print(tombSzam[i])

for szam in tombSzam:
    for i in range(10):
        print(szam*i)

