

class Talo:
    def __init__(self, alinkerros, ylinkerros):
        self.alinkerros = alinkerros
        self.ylinkerros = ylinkerros
        self.hissit = [5]

    def aja_hissia(self, hissin_numero, kohdekerros):
        hissin_numero = self.hissit(hissin_numero)  #pitääkö laittaa -1 koska listan indeksi alkaa nollasta, entä jos hissin eka kerros on myös 0
        if hissin_numero in self.hissit:
            self.siirry_kerrokseen(kohdekerros)



class Hissi:
    def __init__(self):
        self.kerroksessa = 0

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


talo = Talo(0, )