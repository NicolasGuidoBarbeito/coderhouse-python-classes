import sys


def assert_two_inputs():
    if len(sys.argv) != 3:
        print(f'Error - Invalid Arguments\nExample: {sys.argv[0]} [0-10] [0-10]')
        exit(1)


def assert_is_numeric(number_representation):
    if not number_representation.isnumeric():
        print(f'{number_representation} is not a number.')
        exit(1)


def assert_is_between_zero_and_ten(number):
    if number not in range(0, 11):
        print(f'{number} is not between 0 and 10.')
        exit(1)


def validated_inputs():
    assert_two_inputs()
    assert_is_numeric(sys.argv[1])
    assert_is_numeric(sys.argv[2])

    first_grade = int(sys.argv[1])
    second_grade = int(sys.argv[2])

    assert_is_between_zero_and_ten(first_grade)
    assert_is_between_zero_and_ten(second_grade)

    return first_grade, second_grade


first_grade, second_grade = validated_inputs()


if first_grade >= 7 and second_grade >= 7:
    print("Promocionado")
elif first_grade >= 4 and second_grade >= 4:
    print("Aprobado, debe rendir final")
elif first_grade < 4 and second_grade >= 4:
    print("Desaprobado, debe recuperar el primer parcial")
elif first_grade >= 4 and second_grade < 4:
    print("Desaprobado, debe recuperar el segundo parcial")
elif first_grade < 4 and second_grade < 4:
    print("Desaprobó ambos parciales, debe recursar")
