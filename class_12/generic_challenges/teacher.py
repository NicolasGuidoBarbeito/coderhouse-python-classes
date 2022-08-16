class Alumno:
    def __init__(self, legajo, nombre, apellido, documento):
        self.legajo = legajo
        self.nombre = nombre
        self.apellido = apellido
        self.documento = documento

    def __repr__(self):
        return f'{self.apellido}, {self.nombre} - DNI {self.documento} y legajo {self.legajo}'


def main():
    eze = Alumno('1524290', 'Ezequiel', 'Bálsamo', '39624944')
    print(eze)


if __name__ == '__main__':
    main()
