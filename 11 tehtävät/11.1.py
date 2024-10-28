class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi

    def tulosta_tiedot(self):
        print(f"Julkaisun nimi {self.nimi}")


class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja, sivunumero):
        self.kiroittaja = kirjoittaja
        self.sivunumero = sivunumero
        super().__init__(nimi)

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"Kirjan {self.nimi} kirjoittaja on {self.kiroittaja} ja siinä on {self.sivunumero} sivua")



class Lehti(Julkaisu):
    def __init__(self, nimi, paatoimittaja):
        self.paatoimittaja = paatoimittaja
        super().__init__(nimi)

    def tulosta_tieodt(self):
        super().tulosta_tiedot()
        print(f"Lehden {self.nimi} päätoimittaja on {self.paatoimittaja}")

julkaisut = []

julkaisut.append(Lehti("Aku Ankka", "Aki Hyyppä"))
julkaisut.append(Kirja("Hytti n:o 6", "Rosa Liksom", 200))



for j in julkaisut:
    j.tulosta_tiedot()