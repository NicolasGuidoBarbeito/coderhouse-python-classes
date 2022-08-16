"""Tomando la solución del ejercicio anterior anterior, en lugar de devolver None al dividir entre cero, tienes que
capturar una excepción que muestre por pantalla EXACTAMENTE el mensaje: “No se puede dividir entre cero”; si falla el
código
"""


def divide(dividend, divider):
    try:
        return dividend / divider
    except ZeroDivisionError:
        print("Can't divide by zero.")
    except TypeError:
        print("Both operands must be numeric.")


def main():
    divide(10, 2)  # 5.0
    divide(10, 0)  # Can't divide by zero.
    divide('a', 2)  # Both operands must be numeric.
    divide(2, 'a')  # Both operands must be numeric.


if __name__ == '__main__':
    main()
