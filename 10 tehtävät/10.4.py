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

class Kilpailu: 
    def __init__(self, nimi, pituus, autot):
        self.nimi = nimi
        self.pituus = pituus
        self.autot = autot

    def tunti_kuluu(self):
      for auto in self.autot:
            nopeuden_muutos = random.randint(-10, 15)
            auto.kiihdyta(nopeuden_muutos)
            auto.kulje(1)

    def tulosta_tilanne(self):
        print(f"{'Rekisteri':<10}{'Huippunopeus':<15}{'Nopeus':<10}{'Kuljettu matka':<15}")
        print("-" * 50)
        for auto in self.autot:
            print(f"{auto.rekisteritunnus:<10}{auto.huippunopeus:<15}{auto.nopeus:<10}{auto.kuljettu_matka:<15.2f}")
        print()


    def kilpailu_ohi(self):
        for auto in self.autot:
            if auto.kuljettu_matka >= self.pituus:
                return True
        return False

autot = []
for i in range(1, 11):
    rekkari = f"123-{i}"
    huippunopeus = random.randint(100, 200)
    autot.append(Auto(rekkari, huippunopeus))



kilpailu = Kilpailu("Suuri romuralli", 8000, autot)
tunti = 0


print("\nKilpailun tulokset: \n")


while not kilpailu.kilpailu_ohi():
    kilpailu.tunti_kuluu()
    tunti += 1
    if tunti % 10 == 0:
        print(f"Tunti {tunti}")
        kilpailu.tulosta_tilanne()

print("Kilpailu päättyi!")
kilpailu.tulosta_tilanne()