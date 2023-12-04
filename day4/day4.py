def part1():
    file = open("input.txt", "r")
    lines = file.readlines()
    sum = 0
    for line in lines:
        winning, numbers = line[line.index(":") + 1:].split("|") # splits each line into a string of winning numbers and string of numbers you have
        winning = winning.split(" ") # the strings are converts into arrays of string numbers
        numbers = numbers[:-1].split(" ") # gets rid of newline char
        total = 0
        for win in winning:
            if win != '' and win in numbers:
                total += 1
        if total:
            sum += 2 ** (total - 1)
        print(total)
    print(sum)

def part2():
    file = open("input.txt", "r")
    lines = file.readlines()
    totalCards = [1 for _ in range(len(lines))]
    for i, line in enumerate(lines):
        winning, numbers = line[line.index(":") + 1:].split("|")
        winning = winning.split(" ") 
        numbers = numbers[:-1].split(" ")
        total = 0
        for win in winning:
            if win != '' and win in numbers:
                total += 1
        for j in range(1, total + 1):
            totalCards[i + j] += totalCards[i]
    print(sum(totalCards))
part2()