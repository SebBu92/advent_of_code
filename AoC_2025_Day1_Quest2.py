counter = 0
number = 50
with open("aoc_quest1.txt", "r") as quest:
    for values in quest: # textdatei öffnen
        single_value = values.split() # zeilenumbruch der werte in der txt
        for value in single_value: # jede zeile als eigener string
            if value[0] == "L":
                number -= int(value[1:])
                if number == 0 or number == 100:
                    counter += 1
                if (number + 100) < 0:
                    while number < 0:
                        number += 100
                        counter += 1
            if value[0] == "R":
                number += int(value[1:])
                if number == 0 or number == 100:
                    counter += 1
                if (number - 100) > 100:
                    while number > 100:
                        counter += 1
                        number -= 100
print(f"Counter: {counter}")

