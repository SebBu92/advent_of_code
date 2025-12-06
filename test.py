def day1_part2(list):
    counter = 0
    number = 50
    single_value = list.split(", ")
    for value in single_value:
        if value[0] == "L":
            number = number - int(value[1:])
            while number <= 0:
                counter += 1
                number += 100
            print(f"Value: {value}, Number:{number}, Counter: {counter}")
            # if number == 0:
            #     counter += 1
            # print(f"Number:{number}, Counter: {counter}")
            #print(number)
            #print(f"Counter {counter}")
        if value[0] == "R":
            number = number + int(value[1:])
            while number >= 100:
                counter += 1
                number -= 100
            print(f"Value: {value}, Number:{number}, Counter: {counter}")
            # if number == 100:
            #     counter += 1
            # print(f"Number:{number}, Counter: {counter}")
            #print(number)
            #print(f"Counter {counter}")
    print(f"Counter: {counter}")

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
