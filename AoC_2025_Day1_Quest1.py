# Aufgabe 1
def find_zero_values():
    counter = 0
    number = 50
    with open("aoc_quest1.txt", "r") as quest:
        for values in quest: # textdatei öffnen
            value = values.split() # zeilenumbruch der werte in der txt
            for single_value in value: # jede zeile als eigener string
                if single_value[0] == "L":
                    number = (number - int(single_value[1:])) % 100 # modulo 100 sorgt dafür das der bereich 0-99 bleibt
                if single_value[0] == "R":
                    number = (number + int(single_value[1:])) % 100
            if number == 0:
                counter += 1
    print(counter)
find_zero_values()
