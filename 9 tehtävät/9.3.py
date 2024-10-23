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

auto = Auto("ABC-123", 142)

auto.kiihdytä(30)

auto.kulje(0.5)

print(f"Kuljetut kilometrit ovat {auto.km_kuljettu}")

auto.kiihdytä(70)

auto.kulje(2)
print(f"Kuljetut kilometrit ovat {auto.km_kuljettu}")
