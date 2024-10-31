import random

class Auto:
    def __init__(self, rekkari, huippunopeus):
        self.rekkari = rekkari
        self.huippunopeus = huippunopeus
        self.hetk_nopeus = 0
        self.km_kuljettu = 0

    def kiihdytä(self, kiihdytys):
        self.hetk_nopeus += kiihdytys
        if self.hetk_nopeus > self.huippunopeus:
            self.hetk_nopeus = self.huippunopeus
        elif self.hetk_nopeus < 0:
            self.hetk_nopeus = 0

    def kulje(self, tunnit):
        self.km_kuljettu += self.hetk_nopeus * tunnit

autot = []
for i in range(1, 11):
    rekkari = f"123-{i}"
    huippunopeus = random.randint(100, 200)
    autot.append(Auto(rekkari, huippunopeus))

kaynnissa = True
tunnit = 0 

while kaynnissa:
    tunnit += 1

    for auto in autot:
        nopeuden_muutos = random.randint(-10, 15)
        auto.kiihdytä(nopeuden_muutos)
        auto.kulje(1)

        if auto.km_kuljettu >= 10000:
            kaynnissa = False

print("\nKilpailun tulokset: \n")

print(f"{'Rekisteritunnus':<18} {'Huippunopeus':<15}{'Nopeus':<10}{'Kuljettu matka'}")
for auto in autot:
    print(f"{auto.rekkari:<19}{auto.huippunopeus:<15}{auto.hetk_nopeus:<10}{auto.km_kuljettu}")