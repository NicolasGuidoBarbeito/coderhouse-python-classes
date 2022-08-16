from dataclasses import dataclass


@dataclass
class Mamifero:
    cant_mama: int
    esperanza_de_vida: int

    def mamar(self):
        print("Soy un mamífero nadando.")

    def nacer(self):
        print("Soy el mamífero que nació.")


@dataclass
class AnimalMarino:
    tiene_branquias: bool
    especie: str

    def nadar(self):
        print("Soy un animal marino nadando.")


@dataclass
class Cetaceo(Mamifero, AnimalMarino):
    notas: str
    vive_en: str
    peso: float

    def nacer(self):
        print("Soy el cetáceo que nació.")

    def nadar(self):
        print("Soy un cetáceo nadando.")


ballena = Cetaceo(notas='Eubalaena japonica',
                  vive_en='Pacífico norte',
                  peso=60.5,
                  cant_mama=4,
                  esperanza_de_vida=70,
                  tiene_branquias=False,
                  especie='E. japonica')

print(ballena)
ballena.nacer()
ballena.nadar()
ballena.mamar()