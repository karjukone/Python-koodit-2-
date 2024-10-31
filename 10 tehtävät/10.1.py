
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


h = Hissi(0, 15)

h.siirry_kerrokseen(6)
h.siirry_kerrokseen(2)

