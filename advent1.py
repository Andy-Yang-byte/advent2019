# advent of code 2019 day 1

FILE_LOC = "C:\Users\\andyy\Downloads\input.txt"


if __name__ == "__main__":
    f = open(FILE_LOC, "r")
    sum = 0
    for line in f:
        def fuel_calc(value):
            ret = 0
            while True:
                value = (value//3)-2
                if(value <= 0):
                    break
                ret = ret + value
            return ret
        sum = sum + fuel_calc(int(line))
    print(str(sum))