import re

def part1():
    maximum = {
        'red': 12,
        'green': 13,
        'blue': 14
    }

    file = open("input.txt", "r")
    lines = file.readlines()

    sum = 0
    for line in lines:
        if line[-1] == '\n':
            line = line[:-1]
        id = int(re.findall(" .*:", line)[0][1:-1])
        sets = line[line.find(":") + 2:].split(';')
        isValid = True
        for set in sets:
            cubes = set.split(',')
            for cube in cubes:
                if cube[0] == ' ':
                    cube = cube[1:]
                [num, color] = cube.split(' ')
                isValid = isValid and int(num) <= maximum[color]
        if isValid:
            sum += id
    print(sum)

def part2():
    file = open("input.txt", "r")
    lines = file.readlines()

    sum = 0
    for line in lines:
        maximum = {'red': 0, 'green': 0, 'blue': 0}
        if line[-1] == '\n':
            line = line[:-1]
        id = int(re.findall(" .*:", line)[0][1:-1])
        sets = line[line.find(":") + 2:].split(';')
        isValid = True
        for set in sets:
            cubes = set.split(',')
            for cube in cubes:
                if cube[0] == ' ':
                    cube = cube[1:]
                [num, color] = cube.split(' ')
                if int(num) > maximum[color]:
                    maximum[color] = int(num)
        sum += maximum['red'] * maximum['green'] * maximum['blue']
    print(sum)
part2()
