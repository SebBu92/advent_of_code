def find_all_zero_values():
    counter = 0
    number = 50
    with open("AoC_day1.txt", "r") as quest:
        for values in quest: # textdatei öffnen
            single_value = values.split() # zeilenumbruch der werte in der txt
            for value in single_value: # jede zeile als eigener string
                for every_value in range(int(value[1:])):
                    if value[0] == "R":
                        number += 1
                    else:
                        number -= 1
                    
                    if number == -1 or number == 100:
                        number %= 100

                    if number == 0:
                        counter += 1
    print(f"Counter: {counter}")

find_all_zero_values()

