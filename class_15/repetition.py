import sys

if len(sys.argv) != 3:
    print("""Two arguments must be entered.
The first one being the item to repeat.
The second one being the number of repetitions.""")
    exit(1)

item_to_repeat = sys.argv[1]
number_of_repetitions = int(sys.argv[2])

for _ in range(number_of_repetitions):
    print(item_to_repeat)
