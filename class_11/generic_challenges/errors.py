"""En la función de nuestro ejercicio hay un fallo potencial, averigua cuándo sucede y retorna el valor None en ese 
caso especial, en cualquier otro caso devuelve el resultado normal de la función. 

def dividir(a, b):
  return a/b

Pista: Valor indeterminado
"""


def divide(dividend, divider):
    return dividend / divider if divider != 0 else None


def main():
    print(divide(10, 2))    # 5.0
    print(divide(10, 0))    # None


if __name__ == '__main__':
    main()
