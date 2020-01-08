# advent of code 2019 day 10

# x,y (col, row)

if __name__ == "__main__":
    asteroids = []
    f = open('input10.txt', 'r')

    x = 0.0
    y = 0.0
    for line in f:
        for char in list(line):
            if char == '#':  # asteroid found
                asteroids.append((x,y))
            x = x + 1
        x = 0
        y = y + 1
    max = 0
    print(type(x))

    for asteroid in asteroids:
        origin_x = asteroid[0]
        origin_y = asteroid[1]

        slopes = []
        counter = 0

        for asteroid in asteroids:
            
            if asteroid[1] == origin_y:
                if asteroid[0] == origin_x:
                    slopes = []  # reset slopes list
                    continue  # skips origin asteroid
                
            try:
                slope = (asteroid[1] - origin_y) / (asteroid[0] - origin_x)
            except ZeroDivisionError:
                slope = None

            if not slope in slopes:
                counter = counter + 1
                slopes.append(slope)
                if counter > max:
                    max = counter
                    max_coord = (origin_x, origin_y)
    print(max)