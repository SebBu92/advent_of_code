def sum_from_invalidID():
    sum = 0
    with open("AoC_day2.txt", "r") as list:
        for values in list:
            values = values.split(",")
            for value in values:
                value = value.split("-")
                for single_value in range(int(value[0]), int(value[1])):
                    single_value = str(single_value)
                    length = len(single_value)
                    if length == 1:
                        continue
                    if int(single_value[:(length//2)]) == int(single_value[(length//2):]) and length % 2 == 0:
                        sum += int(single_value)
    print(sum)

sum_from_invalidID()