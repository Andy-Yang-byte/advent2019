# advent of code 2019 day 3

# note: this is a very poor algorithm for this purpose - attempting to improve

def get_slope_y_int(point1, point2):
    slope = (point2[1]-point1[1])/(point2[0]-point1[0])
    y_int = 0
    return [slope, y_int]

if __name__ == "__main__":
    f = open('input3.txt', 'r')

    route1 = f.readline().split(',')
    route2 = f.readline().split(',')
    point = [0,0]
    for entry in route1:
        dir = entry[:1]
        num_moves = int(entry[1:])
        if dir == 'U':
            stop = [point[0],point[1]+num_moves]
        elif dir == 'R':
            stop = [point[0]+num_moves,point[1]]
        elif dir == 'D':
            stop = [point[0],point[1]-num_moves]
        elif dir == 'L':
            stop = [point[0]-num_moves,point[1]]
        slope_y_int = get_slope_y_int(point,stop)