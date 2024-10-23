class Auto:
    def __init__(self, rekkari, huippunopeus):
        self.rekkari = rekkari
        self.huippunopeus = huippunopeus
        self.hetk_nopeus = 0
        self.km_kuljettu = 0


auto = Auto("ABC-123", 142)

print(f"Auton rekisteritunnus on: {auto.rekkari:s}, auton huippunopeus on: {auto.huippunopeus:d}, kuljetut matkat: {auto.hetk_nopeus:d} ja ajetut kilomterit: {auto.km_kuljettu:d}")
