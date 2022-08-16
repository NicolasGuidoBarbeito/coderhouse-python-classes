from dates import number_of_seconds_until_next_birthday


birth_day_number = 17
birth_month_number = 4
number_of_seconds = number_of_seconds_until_next_birthday(birth_day_number, birth_month_number)
print(f'{number_of_seconds} seconds left until your next birthday!')
