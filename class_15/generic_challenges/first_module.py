from dataclasses import dataclass


@dataclass(frozen=True, kw_only=True, slots=True)
class Person:
    first_name: str
    last_name: str

    def talk(self):
        return f'Hi, my name is {self.full_name()}'

    def full_name(self):
        return f'{self.first_name} {self.last_name}'
