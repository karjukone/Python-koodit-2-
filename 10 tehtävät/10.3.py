class Hissi:
    def __init__(self, alinkerros, ylinkerros):
        self.alinkerros = alinkerros
        self.ylinkerros = ylinkerros
        self.kerroksessa = alinkerros

    def siirry_kerrokseen(self, kerros):
        if kerros > self.kerroksessa:
            self.ylospain(kerros)
        if kerros < self.kerroksessa:
            self.alaspain(kerros)

    def ylospain(self, alas):
        while self.kerroksessa != alas:
            self.kerroksessa += 1
        print(f"Hissi on kerroksessa {self.kerroksessa}")

    def alaspain(self, ylos):
        while self.kerroksessa != ylos:
            self.kerroksessa -= 1
        print(f"Hissi on kerroksessa {self.kerroksessa}")


class Talo:
    def __init__(self, alin_kerros, ylin_kerros, hissien_lkm):
        self.hissit = [Hissi(alin_kerros, ylin_kerros) for _ in range(hissien_lkm)]
        print(f"Talo luotu, jossa on {hissien_lkm} hissiä, alin kerros {alin_kerros}, ylin kerros {ylin_kerros}.")
        self.palohalutus = self.hissit(siirry_kerrokseen(self.alinkerros))

    def aja_hissiä(self, hissi_numero, kohde_kerros):
        if 0 <= hissi_numero < len(self.hissit):
            print(f"Ajetaan hissiä {hissi_numero} kohdekerrokseen {kohde_kerros}.")
            self.hissit[hissi_numero].siirry_kerrokseen(kohde_kerros)
        else:
            print("Virhe: Hissin numero on virheellinen.")


talo = Talo(1, 10, 3)  
talo.aja_hissiä(0, 5)
talo.aja_hissiä(1, 7)
talo.aja_hissiä(2, 3)
talo.aja_hissiä(0, 1)