"""Crear una clase para trabajar con una Persona. Agregarle 3 atributos de instancia, por lo menos 2 de clase,
el constructor y dos métodos (uno con parámetros y otro sin parámetro).

Luego instanciar a dos personas.
"""


class Person:
    favourite_football_team = 'Lanús'
    wants_a_sallary_in_dollars = True

    def __init__(self, first_name: str, last_name: str, age: int):
        self.__first_name = first_name
        self.last_name = last_name
        self.age = age

    def is_an_adult(self):
        return self.age >= 18

    def is_older_than(self, other_person):
        return self.age >= other_person.age


def main():
    eze = Person('Ezequiel', 'Bálsamo', 26)
    majo = Person('María José', 'Eguía', 23)

    assert eze.is_an_adult()
    assert eze.is_older_than(majo)


if __name__ == '__main__':
    main()
