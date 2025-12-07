def day1_part2(list):
    counter = 0
    number = 50
    single_value = list.split(", ")
    for value in single_value:
        for _ in range(int(value[1:])):
            print(_)
            if value[0] == "R":
                number += 1
            else:
                number -= 1
            
            if number == -1 or number == 100:
                number %= 100

            if number == 0:
                counter += 1
    print(counter)

day1_part2("R1000, L1000, L50, R1, L1, L1, R1, R100, R1")


# R1000 # +10 (50) 10
# L1000 # +10 (50) 20
# L50   # +1  (0)  21
# R1    # +0  (1)  21
# L1    # +1  (0)  22
# L1    # +0  (99) 22
# R1    # +1  (0)  23
# R100  # +1  (0)  24
# R1    # +0  (1)  24
