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


class Sahkoauto(Auto):
    def __init__(self, rekkari, huippunopeus, akkukapasiteetti):
        super().__init__(rekkari, huippunopeus)
        self.akkukapasiteetti = akkukapasiteetti

class Polttomoottoriauto(Auto):
    def __init__(self, rekkari, huippunopeus, bensatankki):
        super().__init__(rekkari, huippunopeus)
        self.bensatankki = bensatankki

sahkoauto = Sahkoauto("ABC-15", 180, 52.5)
polttomoottoriauto = Polttomoottoriauto("ACD-123", 165, 32.3)

sahkoauto.kiihdytä(100)
polttomoottoriauto.kiihdytä(90)

sahkoauto.kulje(3)
polttomoottoriauto.kulje(3)

print(f"Auton {sahkoauto.rekkari} mittarilukema on: {sahkoauto.km_kuljettu}")
print(f"Auton {polttomoottoriauto.rekkari} mittarilukema on: {polttomoottoriauto.km_kuljettu}")