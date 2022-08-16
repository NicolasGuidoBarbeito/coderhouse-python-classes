"""Crear una clase Atleta, que tenga su nombre, apellido, altura,  peso, teléfono e índice de masa corporal (
descripción) . Decidir qué atributos deben ser públicos y cuáles privados. Crear los métodos get y set que crea
necesarios. """

from dataclasses import dataclass


@dataclass(frozen=True, kw_only=True, slots=True)
class Athlete:
    first_name: str
    last_name: str
    height_in_meters: float
    weight_in_kilograms: float
    phone_number: str

    def body_mass_index(self) -> float:
        return self.weight_in_kilograms / (self.height_in_meters ** 2)

    def full_name(self) -> str:
        return f'{self.first_name} {self.last_name}'


def main():
    barbeito = Athlete(first_name='Nicolás',
                       last_name='Barbeito',
                       height_in_meters=1.81,
                       weight_in_kilograms=73,
                       phone_number='1130764259')
    print(barbeito)
    print(f'The body mass index of {barbeito.full_name()} is {barbeito.body_mass_index():.2f}')


if __name__ == '__main__':
    main()
