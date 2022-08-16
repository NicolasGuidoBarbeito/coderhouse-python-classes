from datetime import datetime, timedelta


def next_birth_year_number(birth_day_number: int, birth_month_number: int) -> int:
    today = datetime.today()
    current_year_number = today.year
    current_year_birthday = datetime(current_year_number, birth_month_number, birth_day_number)
    return current_year_number if current_year_birthday > today else current_year_number + 1


def delta_until_next_birthday(birth_day_number: int, birth_month_number: int) -> timedelta:
    year_number = next_birth_year_number(birth_day_number, birth_month_number)
    next_birthday = datetime(year_number, birth_month_number, birth_day_number)
    return next_birthday - datetime.today()


def number_of_seconds_until_next_birthday(birth_day_number: int, birth_month_number: int) -> int:
    return int(delta_until_next_birthday(birth_day_number, birth_month_number).total_seconds())
