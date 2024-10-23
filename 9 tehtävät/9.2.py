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


auto = Auto("ABC-123", 142)

auto.kiihdytä(30)

auto.kiihdytä(70)

auto.kiihdytä(50)
print(f"Auton nopeus on {auto.hetk_nopeus: d} km/h")

auto.kiihdytä(-200)

print(f"Auton nopeus on {auto.hetk_nopeus: d} km/h")